# A1 Museum Ticketing

Write one Python program. It reads a visit day and the visitors' ages, works
out the cheapest correct ticket total, and prints a short summary. The
cheapest total means forming a group whenever a group of 5 adults is possible.

**Do this assignment in a set order.** First reason the rules through in a
chat with your AI assistant and fill in `Specifications.md` in your own words.
Then write the program: either ask the assistant to write it against your
specification, or write it yourself. Then test it.

The full specification is in [brief.md](brief.md).
Read it before you start.

## What is in this folder

| File | What it is |
|---|---|
| `brief.md` | The full specification, the worked examples and how the assignment is graded. Read this first |
| `Specifications.md` | Your worksheet. Fill it in **in your own words, before any code is written**. You submit it |
| `Museum.py` | The starter file. It is a skeleton with `???` placeholders that you complete after the worksheet is done. You submit it |
| `test.py` | Supplied checks. Run them yourself. They are not your test marks |
| `tests.txt` | Your own test cases, up to ten. It starts with one worked example so you can see the format. Replace it and add your own. You submit it |
| Your chat export | Not there yet. Export it from the extension when you finish, and keep the name it gives. You submit it |
| `assignment.json` | Tells the extension which assignment this folder holds. Leave it alone |

## What you need

- Python 3.10 or newer. No extra packages.
- Visual Studio Code.
- The Assignment Guide extension, from the VS Code Marketplace.
- Your course key. We send it to you. It is yours alone.

## Your AI assistant

1. Install the Assignment Guide extension in VS Code.
2. Open this folder in VS Code.
3. Open the Assignment Guide panel and enter your course key.
4. Read the recording notice and agree to it. Nothing is sent until you do.

The key connects the extension to the course server, and the server sends your
messages to a commercial model. The course pays for it. Use the key for this
course only, and do not share it. We can see usage.

The assistant is set up as a tutor. It answers your questions, points out
mistakes, and asks you what you think. It will write code for you once you have
said what the code should do, in your own words. It will not write code you have
not specified, and saying the rules back from the brief does not count as
specifying them.

## Run your program

```sh
python3 Museum.py
```

Type the day, then each age, then `-1`. Use the same order as the worked
examples in the brief.

## Run the supplied checks

From this folder:

```sh
python3 test.py -v
```

On Windows use `py -3 test.py -v`.

**The checks fail at the start.** `Museum.py` is a skeleton, and its `???`
placeholders are not valid Python yet. They pass once your program reproduces
the worked examples exactly.

These checks are not your test marks. Writing your own cases in `tests.txt` is a
separate graded part of the assignment. Work out every expected output by hand
before you run anything.

## The order to work in

1. Read `brief.md` end to end.
2. Open a chat with the assistant and fill in `Specifications.md` first, in your
   own words: the input and output types, then the rules covering the logic, the
   boundaries and the order of the steps. You write the worksheet. The assistant
   answers your questions and checks your reasoning. Finish this before any code
   is written. It is the same reasoning your chat history has to show.
3. Write the program. Either ask the assistant to write it against your
   specification, or write it yourself. The same rubric applies either way.
4. Run `python3 test.py -v`, then your own cases in `tests.txt`. Compare the
   output against the values you worked out by hand.
5. Export your chat history from the extension. Export the whole chat, every
   message, complete and unedited. The extension names the file for you. Keep
   the name it gives you.

## What to submit

1. `Museum.py`, your program.
2. `tests.txt`, up to ten test cases. The format is strict, and the file already
   holds one worked example in it. Work out every expected output by hand before
   you run anything: a case whose expected output you copied from your own
   program proves nothing.
3. `Specifications.md`, your completed worksheet.
4. Your exported chat history, under the name the extension gave it.

See How this is graded in the brief for the marks each part carries.

## Ground rules

- Do not change `test.py`, the brief, or the output format `Museum.py` requires.
- Your worksheet, your code, your test cases and your chat must be your own.
  See Academic integrity in the brief.
- Keep passwords, your student number and API keys out of the chat, out of any
  file the assistant reads, and out of anything you commit to Git. See Tips in
  the brief.
- Your chat history must be a truthful record of how you worked. Export it
  complete and do not edit it afterwards.
- Attacking the assistant or the systems it runs on, including prompt
  injection and using another AI tool to write attack prompts, is covered in
  Academic integrity in the brief.
