const app = new Vue({
	el: '#app',
	data: {
		board: [['', '', ''], ['', '', ''], ['', '', '']],
		player: 'X',
		gameGoing: true,
		status: '',
		singlePlayerMode: false
	},

	methods: {
		boardOnClick(row, column) {
			if(this.board[row][column] === '' && this.gameGoing === true) {
				this.board[row].splice(column, 1, this.player);
				event.preventDefault();

				if(this.player === 'X') {
					this.player = 'O';
				} else {
					this.player = 'X';
				}
			}
			this.checkWinner();
		},

		checkWinner() {
			let player = 'X';
			for(let p = 0; p < 2; p++) {
				for (let i = 0; i < 3; i++) {
					const horizontal =  player === this.board[i][0] && player === this.board[i][1] && player === this.board[i][2];
					const horizontalMid = player === this.board[1][0] && player === this.board[2][0] && player === this.board[3][0];
					const vertical = player === this.board[0][i] && player === this.board[1][i] && player === this.board[2][i];

					const diagnal1 = player === this.board[0][0] && player === this.board[1][1] && player === this.board[2][2];
					const diagnal2 = player === this.board[0][2] && player === this.board[1][1] && player === this.board[2][0];

					if (horizontal || vertical || diagnal1 || diagnal2 || horizontalMid) {
						this.gameGoing = false;
						this.status = 'player ' + player + ' one';
						return;
					} 
				}
				player = 'O';
			}
				
			for (row of this.board) {
				for (column of row) {
					if(column == '') {
						return;
					}
				}
			}
			this.gameGoing = false;
			this.status = 'Its a draw.';
		},

		resetGame() {
			this.gameGoing = true;
			this.board = [['', '', ''], ['', '', ''], ['', '', '']];
			this.player = 'X';
			this.status = '';
		}
	}

});[]