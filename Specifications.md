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

> First, the program should read all the inputs. Since the number of visitors is not given, we should count them one by one.
>
> Then we need to optimize the price of the tickets. To do so, we first need to check how many groups can be formed. Because the group price is always cheaper than the adult price, we need to form as many groups as we can.
>
> After calculated the number of groups, we need to calculate the total price of the tickets. We caluculate this by applying group price, adult price and child price respectively, and consider the date(Weekday, Weekend or holiday) using mulitiple `if` sentences.
>
> Next, we need to add up discount. First, check whether discount can be applied (group_number >= 1, day = weekend or holiday), if possible, calculate the discount. REMEMBER using `float` type to store the number.
>
> Then, we need to calculate the service fee. We first check the day, if the day is weekday, then the service fee is 0. Then if there are 3 people or less, then the service fee is 0. Otherwise for each people there will be $5 service fee charged each, the maximum of the service fee is 30.
> 
> At last we can get the final total cost = the total price of tickets - discount + service fee.

- **Boundaries:** where exactly the behaviour changes as an input changes,
  and what happens on each side.

> First boundary is the group formation. If the (adult_num % 5 == 0), then we can exactly form (adult_num // 5) group(s). However, if the (adult_num % 5 == 4), then 4 of the adults left can not form a new group, in other words, (adult_num // 5) groups can be formed.
>
> Second boundary is the age. If the age of a visitor is 12 years old, then this visitor should be recognized as a child. If a visitor is 13 years old or 59 years old, then this visitor should be recognized as an adult. If a visitor is 60 years old, then this visitor should be recognized as an senior.
>
> Another boundary is the application of discount. if the day is weekday, then the discount should not applied. If no complete group was formed, then the discount should also not applied. Otherwise the discount can be applied.
>
> The last boundary is the service fee.
> First we should check the date type, if the date type is weekday, then service_fee = 0. Next we need check the number of the visitors. If there are 3 visitors or less, then the service_fee = 0. Else if there are 6 visitors or less, then the service_fee = (5 * visitor_num). Otherwise if there are 7 visitors or more, then the service_fee reaches its maximum of 30.
> 
> If the number of visitors <= 6, then the service fee is (visitor_num * 5). But if the number of visitors is 7 or more, then the service fee is capped at 30.

- **Order:** the steps as a numbered list in plain sentences, not Python:
  what must happen first, and what can only be done after input ends?

> 1. The input procedure should be first executed. As all the numbers can be calculated only after that. We use a while function, the loop exits only when the program reads -1.
>
> 2. In the while loop we need to count the number of visitors, since it is not given.
>
> 3. Next, we need to calculate the number of the groups.
>
> 4. Next, we need to calculate the original total ticket prices. First we create the `if` branches in order to distribute different date type. Next, in each branches, we calculate the total ticket prices by seperately calculate the total ticket prices of groups (if possible), adults, children and seniors.
>
> 5. Then we check if the discount can be applied.
>
> 6. Then we calculate the service fee. We use if branches to distribute whether the service fee should be 0 or 30 or less.
>
> 7. At last we organize all the variables and output the result.