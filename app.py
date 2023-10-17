from flask import Flask, render_template

app = Flask(__name__)


# FizzBuzz
@app.route("/fizzbuzz")
def fizzbuzz():
    # 1 - 100
    result = []
    
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            result.append('FizzBuzz')
        elif number % 3 == 0:
            result.append('Fizz')
        elif number % 5 == 0:
            result.append('Buzz')
        else:
            result.append(number)
            
    return render_template("fizzbuzz.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)