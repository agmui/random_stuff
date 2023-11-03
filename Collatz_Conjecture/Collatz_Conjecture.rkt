#lang debug racket
(require racket/trace)
(require debug/repl)
(require benchmark plot/pict racket racket/runtime-path compiler/find-exe)

; collatz conjecture
; if n is even: n/2
; if n is odd 3n+1

; using vector to represent tree
; the index value pair from an edge for the tree 
; values where it is 0 means null

(provide gen-tree)

(define vec-size (expt 1000 2))

(define (update-vec n v)
    (cond [(= n 1) 1] ; base case (gen-tree 1) = 1
          [(not (= (vector-ref v n) 0)) (update-vec (vector-ref v n) v)];TODO:
          [(even? n) (vector-set! v n (/ n 2)) (update-vec (/ n 2) v)]
          [else (vector-set! v n (+(* 3 n)1)) (update-vec (+(* 3 n)1) v)])
)
; standard recursive case
(define (gen-tree n)
    (let ([v (make-vector vec-size)]) ; store result to reuse
        (let rec ([n n])  ; loop though from n to 1
            (update-vec n v)
            (if (= n 1) v (rec (- n 1)))
        )
    )
    (void)
)

; using dp

; using dp and no recursion
(define (gen-tree2 n)
    (let ([v (make-vector vec-size)]) ; store result to reuse
        (for-each (lambda (n) (update-vec n v)) (map add1(range n)))
        ;;; v
    )
)


;;; (trace update-vec)
;;; (trace gen-tree)

(time (gen-tree 700))


(time (gen-tree2 700))