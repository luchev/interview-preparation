interface Player {
    num: number;
    hand: string;
    opponents: number[];
};

let handMap = {
    'C': ['P', 'L'],
    'P': ['R', 'S'],
    'R': ['L', 'C'],
    'L': ['S', 'P'],
    'S': ['C', 'R'],
};

const N: number = parseInt(readline());
let players: Player[] = [];
for (let i = 0; i < N; i++) {
    var inputs: string[] = readline().split(' ');
    const NUMPLAYER: number = parseInt(inputs[0]);
    const SIGNPLAYER: string = inputs[1];
    players.push({
        num: NUMPLAYER,
        hand: SIGNPLAYER,
        opponents: [],
    });
}

while (players.length > 1) {
    let p1 = players.shift();
    let p2 = players.shift();

    if (p1.hand === p2.hand) {
        if (p1.num < p2.num) {
            p1.opponents.push(p2.num);
            players.push(p1);
        } else {
            p2.opponents.push(p1.num);
            players.push(p2);
        }
    } else if (handMap[p1.hand].includes(p2.hand)) {
        p1.opponents.push(p2.num);
        players.push(p1);
    } else if (handMap[p2.hand].includes(p1.hand)) {
        p2.opponents.push(p1.num);
        players.push(p2);
    }
}

console.log(players[0].num);
console.log(players[0].opponents.join(' '))
