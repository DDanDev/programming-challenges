//prepare
const inLine = document.getElementById("input");
const output = document.getElementById("output");

let debugMessages = false
function log(msg) {
	if (debugMessages) log(msg)
}

function printOut(...content) {
	actuallyPrint(content, "outLog");
}

function printSys(...content) {
	actuallyPrint(content, "sysLog");
}

function actuallyPrint(content, className) {
	log(`${className}: ${content}`);
	output.innerHTML += `<p class="${className}">${String(content).replace(/ /gi, "&nbsp")}</p>`;
}

function unprint() {
	output.querySelector(":nth-last-child(1)").remove();
}

let tempinput = "";
let listener = (e) => {
	tempinput = e.target.value;
	actuallyPrint(`>>${e.target.value}`, "inLog");
	e.target.value = "";
	e.target.id = "";
	log("returning input: " + tempinput);
};
inLine.addEventListener("change", listener);

async function input(msg) {
	inLine.id = "inActive";
	inLine.placeholder = msg ? msg : "type input";
	inLine.focus();
	tempinput = "";
	return new Promise((res) => {
		let waiting = setInterval(() => {
			if (tempinput) {
				clearInterval(waiting);
				res(tempinput);
			}
		}, 200);
	});
}

//menu
let listofapps = ["dancingSentence", "balloons", "sudoku"];
printSys(`pseudo cli to practice js coding with input and output`);
async function startCLI() {
	printSys(`<hr>`);
	printSys("choose: " + listofapps.join(", "));
	let choose = await input("iniciar: ");
	if (listofapps.includes(choose)) eval(choose + "()");
	else startCLI();
}
startCLI();

//modules
async function dancingSentence() {
	printSys(">>Dancing Sentences started<<");
	//////code
	while (true) {
		let sentence = await input("type a sentence or '*exit*'");
		if (sentence === "*exit*") break;
		let toupper = true;
		let dancing = "";
		for (let char of sentence) {
			if (toupper) dancing += char.toUpperCase();
			else dancing += char.toLowerCase();
			if (char !== " ") {
				toupper = !toupper;
			}
		}
		printOut(dancing);
	}
	////////end
	startCLI();
}

async function balloons() {
	printSys(">>Balloons started<<");
	//////code
	while (true) {
		let rows, cols, pos;
		while (true) {
			[rows, cols, pos] = (await input("Rows, Cols, Entry Col (integers separated by a space) - 0 0 0 to exit")).split(" ").map((x) => parseInt(x));
			if (!(isNaN(rows) || isNaN(cols) || isNaN(pos))) break;
		}
		if (rows === 0 && cols === 0 && pos === 0) break;

		let row, brokeat, leftfani, rightfani;
		pos--;
		brokeat = false;
		for (let rowi = 0; rowi < rows; rowi++) {
			(leftfani = undefined), (rightfani = undefined);
			row = (await input(`${cols} ventiladores da fileira ${rowi + 1}`)).split(" ").map((x) => parseInt(x));
			if (row[pos] !== 0) {
				printOut(`BOOM ${rowi + 1} ${pos + 1}`);
				brokeat = rowi;
				break;
			} else {
				for (let searchi = pos - 1; searchi > -1; searchi--) {
					if (row[searchi] !== 0) {
						leftfani = searchi;
						break;
					}
				}
				for (let searchi = pos + 1; searchi < cols; searchi++) {
					if (row[searchi] !== 0) {
						rightfani = searchi;
						break;
					}
				}
				pos += (row[leftfani] ? row[leftfani] : 0) - (row[rightfani] ? row[rightfani] : 0);
				if (pos <= leftfani) {
					printOut(`BOOM ${rowi + 1} ${leftfani + 1}`);
					brokeat = rowi;
					break;
				} else if (pos >= rightfani) {
					printOut(`BOOM ${rowi + 1} ${rightfani + 1}`);
					brokeat = rowi;
					break;
				} else if (pos <= 0) pos = 0;
				else if (pos >= cols - 1) pos = cols - 1;
			}
		}
		if (brokeat === false) printOut(`OUT ${pos + 1}`);
		else {
			for (let i = brokeat + 1; i < rows; i++) {
				await input(`ventiladores da fileira (pode pular, ja explodiu)${i + 1}`);
			}
		}
	}
	////////end
	startCLI();
}
async function sudoku() {
	printSys(">>sudoku verifier started<<");
	//////code
	let mistakeInSet = (sudokuSet, group) => {
		let founderror = false;
		for (let subseti in sudokuSet) {
			if (!(new Set(sudokuSet[subseti]).size === 9)) {
				log(subseti);
				printOut(`Incorrect at ${group} ${parseInt(subseti) + 1}`);
				founderror = true;
			}
		}
		return founderror;
	};
	while (true) {
		//get input for sudoku table, validating each input
		let sudokutable = [];
		let promptmsg = (resetpromptmsg = "enter sudoku line or *exit*");
		try {
			for (let i = 0; i < 9; i++) {
				log(`input n ${i + 1}`);
				try {
					sudokutable.push(
						(await input(promptmsg)).split(" ").map((x) => {
							if (x === "*exit*") throw x;
							if (`${x}`.match(/[a-z]/gi)) throw "incorrect";
							x = parseInt(x);
							if (isNaN(x) || x < 1 || x > 9) throw "incorrect";
							return x;
						})
					);
					if (sudokutable[sudokutable.length - 1].length !== 9) {
						sudokutable.pop()
						throw "incorrect";
					}
					promptmsg = resetpromptmsg;
				} catch (err) {
					if (err === "incorrect") {
						i--;
						log(`repeating line`);
						promptmsg = "insert last line again or *exit*";
						unprint();
					} else throw err;
				}
				log(`table: [[${sudokutable.join("], [")}]]`);
			}
		} catch (err) {
			break;
		}
		log(`finished table:`, sudokutable);
		
		//check lines
		let mistakefound = mistakeInSet(sudokutable, "row") ? true : false;

		//list columns
		let rotate = [];
		for (let row = 0; row < 9; row++) {
			rotate[row] = [];
			for (let column = 0; column < 9; column++) {
				rotate[row][column] = sudokutable[column][row];
			}
		}
		//check columns
		mistakefound = mistakeInSet(rotate, "column") ? true : mistakefound;

		//list blocks
		let blocks = [];
		for (let rowgroup = 0; rowgroup < 3; rowgroup++) {
			for (let colgroup = 0; colgroup < 3; colgroup++) {
				let pieces = sudokutable.slice(rowgroup * 3, rowgroup * 3 + 3).map((x) => x.slice(colgroup * 3, colgroup * 3 + 3));
				blocks.push([...pieces[0], ...pieces[1], ...pieces[2]]);
			}
		}
		//check blocks
		mistakefound = mistakeInSet(blocks, "block") ? true : mistakefound;

		if (!mistakefound) printOut("Correct sudoku resolution! Start again or *exit*");
		else printOut("Try again or *exit*");
	}
	////////end
	startCLI();
}
