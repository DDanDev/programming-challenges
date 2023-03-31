//prepare
const inLine = document.getElementById("input");
const output = document.getElementById("output");

function printOut(content) {
	console.log(`print: ${content}`);
	output.innerHTML += `<p class="outLog">${content}</p>`;
}

function printSys(content) {
	console.log(`sys: ${content}`);
	output.innerHTML += `<p class="sysLog">${content}</p>`;
}

function input(msg, vartarget, code) {
	// enableInput(msg);
	inLine.id = "inActive";
	inLine.placeholder = msg ? ">> " + msg : ">> type input";
	let listener = (e) => {
		//assign var
		window[vartarget] = e.target.value;
		//log and clear
		// handleInput(e);
		output.innerHTML += `<p class="inLog">>>${e.target.value}</p>`;
		e.target.value = "";
		e.target.id = "";
		inLine.removeEventListener("change", listener);
		//do
		console.log("var " + vartarget + " = " + window[vartarget]);
		if (code) code();
	};
	inLine.addEventListener("change", listener);
    // debugger;
}

printSys(`pseudo cli to practice js coding with input and output<hr />`);
//code
printSys(">>Dancing Sentences started<<");
(function dancingSentence() {
	input("", "sentence", () => {
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
		dancingSentence();
	});
})();
//end
