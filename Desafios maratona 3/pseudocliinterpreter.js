//prepare
const inLine = document.getElementById("input");
const output = document.getElementById("output");

function printOut(...content) {
	actuallyPrint(content, "outLog");
}

function printSys(...content) {
	actuallyPrint(content, "sysLog");
}

function actuallyPrint(content, className) {
	console.log(`${className}: ${content}`);
	content = String(content).replace(/ /gi, "&nbsp");
	output.innerHTML += `<p class="${className}">${content}</p>`;
}

async function input(msg) {
	// enableInput(msg);
	inLine.id = "inActive";
	inLine.placeholder = msg ? ">> " + msg : ">> type input";
	let tempinput = "";
	let listener = (e) => {
		//assign var
		tempinput = e.target.value;
		//log and clear
		// handleInput(e);
		actuallyPrint(`>>${e.target.value}`, "inLog");
		e.target.value = "";
		e.target.id = "";
		inLine.removeEventListener("change", listener);
		//do
		console.log("returning input: " + tempinput);
	};
	inLine.addEventListener("change", listener);
	await new Promise((resolve) => {
		let waiting = setInterval(() => {
			if (tempinput) {
				clearInterval(waiting);
				resolve();
			}
		}, 200);
	});
	return tempinput;
}
listofapps = ["dancingSentence", "balloons"];
printSys(`pseudo cli to practice js coding with input and output`);
async function startCLI() {
	printSys(`<hr>`);
	printSys("choose: " + listofapps.join(", "));
	let choose = await input("iniciar: ");
	if (listofapps.includes(choose)) eval(choose + "()");
	else startCLI();
}
startCLI();
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
		let [rows, cols, pos] = (await input("Rows, Cols, Entry Col (integers separated by a space) - 0 0 0 to exit")).split(" ").map((x) => parseInt(x));
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

		// debugger;
	}

	////////end
	startCLI();
}
