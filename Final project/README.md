# ONLINE STORE
#### Video Demo:  https://youtu.be/pgbceVzUfJk
#### Description: The software, written in Python, implements an online store for the user, where the client can choose the product, he needs (in particular, a cell phone), based on a specific model or based on the user’s budget. Also, code provides functionality of calculation credit for the cellphone with payment schedule in excel file or creating invoice in pdf.

<a name="readme-top"></a>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
        <a href="#built-with">Built With</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#tests">Test</a></li>
    <li><a href="#tips-and-issues">Tips and issues</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

### Built With

* Visual Studio Code [cs50.dev](https://cs50.dev/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

The project requires installation of the following libraries.
Please copy and run in terminal following lines below according instructions.


### Prerequisites

* emoji
  ```sh
  pip install emoji
  ```
* pandas
  ```sh
  pip install pandas
  ```
* openpyxl
  ```sh
  pip install openpyxl
  ```
* fpdf
  ```sh
  pip install fpdf2
  ```
    > [!CAUTION]
    > Please be sure to install exactly fpdf2 library with 2 at the end.
* datetime
  ```sh
  pip install DateTime
  ```

### Installation

1. Open the terminal on VS Code.

2. Copy and paste (or type) line of emoji library for instalation.
   ```sh
   pip install emoji
   ```

3. Then run the line.

4. Be sure that the library installed seccesfully.

5. Now you are ready to install other four libraries. Follow steps from 1 to 4.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage

### Preface:

After the lines of code that import the libraries, the program contains input data that the coder can change if desired without fear of breaking the code.
```sh
  phone_model = ["SMALL Phone", "ReGuLaR Phone", "huge Phone"]
  value = ["budget", "midrange", "expensive"]
  cost = [429, 799, 999]
  annual_interest_rate = 8
   ```

### Main part of code

The main function consists of three main parts.
```sh
def main():
    ...
  ```

The first independent part can be used separately. It defines the input data into the program, giving the user the opportunity to select a phone based on his interests. Queries are constructed in such a way that error-insensitive and/or case-insensitive input is available to the user.
```sh
  while True:
      try:
          user_choice = input(f'Please choose your cell phone from criteria (exact item or by value) below:\n {", ".join(phone_model)}\n or\n {", ".join(value)}\nMy choise is: ').strip()
          ...
```

The second part of the main function is used to call the **function_1(user_choice)** in order to determine the price of the phone for further calculations. It also allows the user to change their decision once desired. If the user agrees with the primary decision, the program proceeds to the next action - the third part of the code.
```sh
  while True:
      try:
          user_selection = function_1(user_choice)
          ...
```

The third part of the main function of the code uses the ability not only to define a request to pay the full cost of the phone or provide a loan calculation (and create an excel file). But is also used to call the **function_2(loan_amount, loan_term_months, annual_interest_rate)** to calculate the credit or is used to call the **function_n(phone_to_invoice)** to return message required to create an invoice (in pdf format).
```sh
  while True:
      try:
          payment = input('Do you want to pay the entire amount at once or arrange for monthly installments?\n Please choose "Total" or "Mothly Installments": ').strip().lower()
          ...
```

The first **def function_1(choice):** is used to not only determine the cost of a phone based on the entered data of a specific phone, but also has the ability to help the user return the value of the name of a specific phone model and its cost if the user himself has not decided on a choice but is only counting on a certain budget.
```sh
def function_1(choice):
    if choice == phone_model[0]:
        return f"Price for your phone is: {cost[0]}"
    ...
    elif choice == value[1]:
        return f"Price for your {phone_model[1]} is {cost[1]}"
    else:
        return f"Price for your {phone_model[2]} is {cost[2]}"
```

The second **def function_2(cost, loan_term_months, annual_interest_rate):** is used to calculate and display loan data. It is divided into two parts. The first part displays data based on the fact that the user enters only one month of lending. The second part carries out calculations from two months.
```sh
def function_2(cost, loan_term_months, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / loan_term_months / 100
    ...
```

The third and last one **def function_n(phone):** is used to display a message on an invoice indicating a pre-selected phone number by the user and calculating the expiration date of the invoice or voucher (in this case, a delta of 14 days was selected).
```sh
def function_n(phone):
    expiration_date = date.today() + timedelta(days=14)
    ...
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Tests

Separately in the file **test_project.py** unit tests are created to test each of the project functions:

```sh
def test_function_1():

def test_function_2():

def test_function_n():
```

Tests have even been created for data entry that cannot be created during normal use of the program. For example, like entering digits and numbers into a function (which cannot be done by the user in a normal using of the program, there are restrictions on incorrect/incorrect/insufficient/excessive data input).

```sh
def test_function_1():
    ...
    assert function_1("cat") == "Price for your huge Phone is 999"
    assert function_1(0) == "Price for your huge Phone is 999"

    with pytest.raises(TypeError):
        function_1()
```

```sh
def test_function_2():
    ...
    with pytest.raises(ZeroDivisionError):
        function_2(0, 0, 0)
    with pytest.raises(ZeroDivisionError):
        function_2(100, 0, 10)
    with pytest.raises(TypeError):
        function_2(100, 10)
    with pytest.raises(TypeError):
        function_2(100, 10, "cat")
```

```sh
def test_function_n():
    ...
    assert function_n("cat") == 'This is a certificate for your new "cat". Validation only for 14 days till 2024-01-21.'
    assert function_n(0) == 'This is a certificate for your new "0". Validation only for 14 days till 2024-01-21.'

    with pytest.raises(TypeError):
        function_n()
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Tips and issues

> [!NOTE]
> Unfortunately, **Visual Studio Code** in **Codespace** cannot open a file with an excel extension, so the functionality of displaying the loan calculation on the screen was implemented.

> [!CAUTION]
> When testing a function **def test_function_n():** it is necessary to change the date, which must be the result of testing the function, otherwise the test will ***fail***. For example, if testing is carried out on January 1, 2024, then it is ***necessary*** to rewrite the date of the message in the code, adding 14 days. That is, the **assert** function should be on the date 2024-01-14.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Iaroslav Smirnov - mrricoford@gmail.com

Project presentation: [https://youtu.be/pgbceVzUfJk](https://youtu.be/pgbceVzUfJk)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Acknowledgments

Many thanks to
* David J. Malan Gordon McKay Professor of the Practice of Computer Science at Harvard University in the School of Engineering and Applied Sciences for passion and professionalism [https://cs.harvard.edu/malan/](https://cs.harvard.edu/malan/)
* Harvard University for high quality education [https://www.harvard.edu/](https://www.harvard.edu/)
* and to edX for opportunity to learn and improve [https://www.edx.org/](https://www.edx.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
