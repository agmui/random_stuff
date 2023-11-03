#lang racket

(require benchmark plot/pict racket racket/runtime-path compiler/find-exe)
(define-runtime-path fib-path
  "./Collatz_Conjecture.rkt")
(define-runtime-path collatz-path
  "./Collatz_Conjecture.rkt")
(define-runtime-path compiled-dir
  "./compiled")
(define results
  (run-benchmarks
   ; files to run (whats)
   (list collatz-path);(list fib-path collatz-path)
   ; list of options (hows)
   (list (list 'jit 'no-jit))
   ; how to run each benchmark
   (lambda (file jit)
     (if (equal? jit 'jit)
         (system* (find-exe) file)
         (system* (find-exe) "-j" file)))
   #:build
   (lambda (file jit)
     (system* (find-exe) "-l" "raco" "make" file))
   #:clean
   (lambda (file jit)
     (system* (find-executable-path "rm") "-r" "-f" compiled-dir))
   #:num-trials 3;0
;;;    #:make-name (lambda (path)
;;;                  (let-values
;;;                      ([(1 file-name 2) (split-path path)])
;;;                    (path->string file-name)))
                   ))
(parameterize ([plot-x-ticks no-ticks])
  (plot-pict
   #:title "jit vs no jit"
   #:x-label #f
   #:y-label "normalized time"
   (render-benchmark-alts
    ; default options
    (list 'jit)
    results)))