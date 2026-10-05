# A1 Museum Ticketing: My Specifications

**Finish this file first, before any code is written.** You supply the
reasoning and fill in this worksheet in your own words. The AI can then
write the code against it.

## Input and output types

What the program reads and what it prints, with the type of each value:
int, float, str, bool. Say why.

- **Inputs:** what values does the program read, and what type is each?

> It firstly reads the day type (interger type, 1-5 = weekday, 6-7 = weekend, 8 = holiday), and reads the visitors' ages respectively (interger type between [0, 80]).
> 
> The visitors' count is not given, so we need to use a `while` loop.

- **Outputs:** what does the program print, what type is each value, and
  how are the money values printed?

> It firstly prints the day type. It consists a string ("weekend / weekday / holiday"). Then we need to print the count of different types of people and the total count (integers). Then we need to print the groups formed (integers). In the last, we need to calculate the discount, survice fee and the total cost. It can be integers or floats if discount applied. Since the format of money values are printed in floats (approx. to 2 digits) and for calculation convenience, it is more suitable to store them as floats in the program.

## The rules in my own words

State what the program must do, in your own words, not the assignment's
wording pasted back. Work through each part below:

- **Logic:** what the program must do, rule by rule.
- **Boundaries:** where exactly the behaviour changes as an input changes,
  and what happens on each side.
- **Order:** the steps as a numbered list in plain sentences, not Python:
  what must happen first, and what can only be done after input ends?
