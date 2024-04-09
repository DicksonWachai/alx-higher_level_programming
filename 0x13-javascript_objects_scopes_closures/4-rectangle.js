#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        } else {
            return undefined;
        }
    }
    print() {
        for (let i = 0; i < this.height; i++)
        {
            let row = "";
            for (let j = 0; j < this.width; j++)
            {
                row += 'X';
            }
            console.log(row);
            }
    }
    double() {
        this.width = this.width * 2;
        this.height = this.height * 2;
        for (let i = 0; i < this.height; i++) {
            let row = "";
            for (let j = 0; j < this.width; j++) {
                row += 'X';
            }
            console.log(row)
        }
    }
    rotate() {
        let temp;
        temp = this.height;
        this.height = this.width;
        this.width = temp;
        for (let i = 0; i < this.height; i++) {
            let row = "";
            for (let j = 0; j < this.width; j++) {
                row += 'X';
            }
            console.log(row);
        }
    }
}
module.exports = Rectangle;