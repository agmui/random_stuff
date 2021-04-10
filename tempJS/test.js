const fs = require('fs')
const cards = require('./sort.json')

let data = [
    [ 'Upgrade',
        ['Move'],
        ['Ban'],
        ['Other']
    ]
]

//=============================

/*for(let i of cards) {
    if (i.type === 'Upgrade'){
        data[0].push(i)
    }
    else if (i.type === 'Downgrade'){
        data[1].push(i)
    }
    else if (i.type === 'Magic'){
        data[2].push(i)
    }
}*/
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

for (let i of cards[0]) {
    console.log(i.text)
    readline.question('input: ', input => {
        console.log(`chose: ${input}`)
        console.log('==========================\n')
        readline.close();
        if (input === 'a'){//move
            data[0][1].push(i)
        } else if (input === 'b'){//ban
            data[0][2].push(i)
        } else if (input === 'c'){//other
            data[0][3].push(i)
        }
    });
}



//=============================

fs.writeFile('./sort2.json', JSON.stringify(data), (err) => {
    if (err) throw err;
})