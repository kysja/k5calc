# k5calc - Simple Windows Keyboard Calculator

k5calc is a simple Windows keyboard calculator built with Python and the Tkinter framework. 
It allows you to perform basic arithmetic calculations using only your keyboard, without the need to click on a calculator app.

![k5calc](https://user-images.githubusercontent.com/55608637/210726044-781792aa-d267-41f0-8691-294226ce9925.png)


## Features

- Perform basic arithmetic calculations (addition, subtraction, multiplication, division, power of n, square root)
- Use the keyboard to enter numbers and operators
- Display the calculation history and results
- Customizable hotkey to show and hide the calculator 
- For lexing and parsing, the [SLY](https://sly.readthedocs.io/en/latest/sly.html) library was used.


## Download

1. [Download](https://github.com/kysja/k5calc/raw/master/download/k5calc.zip) zip file 
2. Extract the zip file to a local directory
3. (Optional) Open config.ini and change the hide/show calculator hotkey (Default - **Ctrl-Alt-C**)
3. Run **k5calc.exe**

## How to use

- The default hotkey to hide/show the calculator is **Ctrl-Alt-C**
- Press **<Enter>** to get the result of calculation
- After the second calculation, a history button will appear
- Use **config.ini** to set the hide/show hotkey, background color, and fonts
- See the list of supported operators below

### Operators

- a+b : Addition
- a-b : Subtraction
- a*b : Multiplication
- a/b : Division
- a^n : Power of N
- sqrt(a) : Square root
- (a+b) : Parentheses



## Credits

k5calc was developed by Alex Ulogov.

## License

k5calc is released under the [MIT License](https://github.com/kysja/k5calc/blob/b65da43aa81a42fc4ad7d41a44fe1d748319d140/LICENSE).

