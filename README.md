# Altranmas 2020 Coding Challenge 🎅

## Instructions
Clone this repository and run the generate_input.py script with your name as follows:

```
python generate_input.py --name <Your Name Here>
```

You can use any language you like to take part. However, make sure you are using python 3 to generate the input. If you don't have python 3, contact me and I can generate an input for you.

When you have completed the challenge, head to [this repository](https://github.com/rej696/altranmas2020-answers) to generate your answer.

🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄

## Part One

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf traffic controller at the North Pole tells him where to move next. The elf consults it's XFacts software \(Courtesy of Altranmas Corp.\) to determine a suitable direction for Santa to move his sleigh. Moves are always exactly one house to the north \(^\), south \(v\), east \(>\), or west \(<\). After each move, Santa delivers another present to the house at his new location.

However, unbeknownst to Santa or the elf traffic controller, there is a critical bug in the software and so the directions are a little off... Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

- \> delivers presents to 2 houses: one at the starting location, and one to the east.
- ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
- ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

🎅🎅🎅🎅🎅🎅🎅🎅🎅

## Part Two
The next year, to speed up the process, Santa hires an apprentice, Neil, to deliver presents with him.

Santa and Neil start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf traffic controller, who is still using the same buggy software as the previous year.

This year, how many houses receive at least one present?

For example:

- ^v delivers presents to 3 houses, because Santa goes north, and then Neil goes south.
- ^>v< now delivers presents to 3 houses, and Santa and Neil end up back where they started.
- ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Neil going the other.

Use the same input as before.

🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄
