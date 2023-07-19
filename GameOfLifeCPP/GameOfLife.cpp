#include<iostream>
#include<string>
using namespace std;
const int gridWidth = 20;
const int gridHeight = 20;
char grid[gridHeight][gridWidth];
char critter = '*';
char dead = ' ';
void initializeGrid() {
	for (int i = 0; i < gridHeight; i++) {
		for (int j = 0; j < gridWidth; j++) {
			int randNum = rand() % 2;
			if (randNum == 0) {
				grid[i][j] = dead;
			}
			else {
				grid[i][j] = critter;
			}
		}
	}
}
void printGrid() {
	for (int i = 0; i < gridHeight; i++) {
		for (int j = 0; j < gridWidth; j++) {
			cout << grid[i][j];
			if (j < gridWidth - 1) {
				cout << "|";
			}
		}
		if (i < gridHeight - 1) {
			cout << endl << "-";
			for (int k = 1; k < gridWidth; k++) {
				cout << "+-";
			}
			cout << endl;
		}
	}
	cout << endl;
}
int getNeighbours(int i, int j) {
	int aliveNeighbours = 0;
	if (i + 1 < gridHeight) {
		if (grid[i + 1][j] == critter) {
			aliveNeighbours++;
		}
	}
	if (j + 1 < gridWidth) {
		if (grid[i][j + 1] == critter) {
			aliveNeighbours++;
		}
	}
	if (i - 1 >= 0) {
		if (grid[i - 1][j] == critter) {
			aliveNeighbours++;
		}
	}
	if (j - 1 >= 0) {
		if (grid[i][j - 1] == critter) {
			aliveNeighbours++;
		}
	}
	if (i + 1 < gridHeight && j + 1 < gridWidth) {
		if (grid[i + 1][j + 1] == critter) {
			aliveNeighbours++;
		}
	}
	if (i - 1 >= 0 && j - 1 >= 0) {
		if (grid[i - 1][j - 1] == critter) {
			aliveNeighbours++;
		}
	}
	if (i - 1 >= 0 && j + 1 < gridWidth) {
		if (grid[i - 1][j + 1] == critter) {
			aliveNeighbours++;
		}
	}
	if (i + 1 < gridHeight && j - 1 >= 0) {
		if (grid[i + 1][j - 1] == critter) {
			aliveNeighbours++;
		}
	}
	return aliveNeighbours;
}
void createNextState() {
	char nextGrid[gridHeight][gridWidth];
	for (int i = 0; i < gridHeight; i++) {
		for (int j = 0; j < gridWidth; j++) {
			int aliveNeighbours = getNeighbours(i, j);
			if (grid[i][j] == critter) {
				if (aliveNeighbours == 2 || aliveNeighbours == 3) {
					nextGrid[i][j] = critter;
				}
				else {
					nextGrid[i][j] = dead;
				}
			}
			else {
				if (aliveNeighbours == 3) {
					nextGrid[i][j] = critter;
				}
				else {
					nextGrid[i][j] = dead;
				}
			}
		}
	}
	for (int i = 0; i < gridHeight; i++) {
		for (int j = 0; j < gridWidth; j++) {
			grid[i][j] = nextGrid[i][j];
		}
	}
}
int main() {
	srand(time(0));
	initializeGrid();
	printGrid();
	int generations = 0;
	while (1) {
		string input;
		cout << "Enter (n)ext or (q)uit\n";
		cin >> input;
		if (input == "q") {
			break;
		}
		else {
			createNextState();
			printGrid();
			generations++;
			cout << "Generation: " << generations << endl;
			cout << "\n\n\n";
		}
	}
	return 0;
}