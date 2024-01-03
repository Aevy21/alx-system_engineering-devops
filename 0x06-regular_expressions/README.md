# Regular Expressions README

## Overview

This README provides a comprehensive guide to understanding and utilizing regular expressions (regex). Regular expressions are powerful tools for pattern matching and manipulation of text data. Whether you're a beginner or an experienced developer, this guide will help you navigate the world of regex.

## Table of Contents

1. [Introduction](#introduction)
2. [Basic Syntax](#basic-syntax)
3. [Metacharacters](#metacharacters)
4. [Quantifiers](#quantifiers)
5. [Character Classes](#character-classes)
6. [Anchors](#anchors)
7. [Groups and Capturing](#groups-and-capturing)
8. [Modifiers](#modifiers)
9. [Lookarounds](#lookarounds)
10. [Common Use Cases](#common-use-cases)
11. [Best Practices](#best-practices)
12. [Resources](#resources)

## Introduction

Regular expressions are sequences of characters that define search patterns. They are widely used in programming, text processing, and data validation. Understanding regex is a valuable skill for anyone dealing with textual data.

## Basic Syntax

Regex patterns consist of ordinary characters and metacharacters. Learn the basics of constructing patterns and using common symbols.

## Metacharacters

Explore the meaning and usage of metacharacters like `^`, `$`, `.`, `*`, `+`, `?`, etc., in regex patterns.

### Examples:

- `^start`: Matches any string that starts with "start."
- `end$`: Matches any string that ends with "end."
- `.\*`: Matches any sequence of characters.

## Quantifiers

Understand how quantifiers like `*`, `+`, `?`, and `{}` control the number of occurrences of characters in a pattern.

### Examples:

- `a*`: Matches zero or more occurrences of the character 'a.'
- `b+`: Matches one or more occurrences of the character 'b.'
- `c?`: Matches zero or one occurrence of the character 'c.'
- `d{2,4}`: Matches 2 to 4 occurrences of the character 'd.'

## Character Classes

Learn about character classes (`[...]`) and how they simplify matching sets of characters.

### Examples:

- `[aeiou]`: Matches any vowel.
- `[^0-9]`: Matches any non-digit character.

## Anchors

Discover the importance of anchors (`^` and `$`) in specifying where a pattern should match within the text.

### Examples:

- `^\d{3}`: Matches a string starting with three digits.
- `\bword\b`: Matches the word "word" as a whole word.

## Groups and Capturing

Explore how to create groups in regex patterns and capture specific portions of matched text.

### Examples:

- `(\d{2})-(\d{2})-(\d{4})`: Captures day, month, and year in a date format.

## Modifiers

Understand modifiers like `i`, `g`, `m`, etc., that influence the behavior of regex patterns.

### Examples:

- `/pattern/i`: Performs case-insensitive matching.

## Lookarounds

Learn about positive and negative lookaheads/lookbehinds for more advanced pattern matching.

### Examples:

- `(?<=@)\w+`: Matches the username in an email address.

## Common Use Cases

Explore practical examples of regex for tasks such as validation, extraction, and substitution.

## Best Practices

Gain insights into writing efficient and maintainable regular expressions with best practices.

## Regex Examples Table

| **Regex Pattern** | **Description**                                      | **Example Match**                   |
|-------------------|------------------------------------------------------|-------------------------------------|
| `abc`             | Literal match: matches the exact characters "abc"     | "abc" in "The abc is here."         |
| `.`               | Wildcard: matches any single character               | "a.c" matches "abc" in "a-c"        |
| `^`               | Anchors the match at the beginning of a line         | `^Start` matches "Start of text"    |
| `$`               | Anchors the match at the end of a line               | `end$` matches "end of text"        |
| `[]`              | Character class: matches any one of the characters inside the brackets | `[aeiou]` matches any vowel    |
| `[^]`             | Negated character class: matches any character not listed | `[^0-9]` matches non-digits     |
| `*`               | Zero or more occurrences of the preceding element    | `ab*c` matches "ac" and "abc"       |
| `+`               | One or more occurrences of the preceding element    | `ab+c` matches "abc" but not "ac"   |
| `?`               | Zero or one occurrence of the preceding element     | `ab?c` matches "ac" and "abc"       |
| `()`              | Grouping: groups multiple tokens together           | `(abc)+` matches "abc" or "abcabc" |
| `\`               | Escape character: treats the next character as a literal, not a special character | `a\*b` matches "a*b"     |
| `|`               | Alternation: matches either the pattern on the left or the one on the right | `cat|dog` matches "cat" or "dog" |
| `\A`              | Start of string                                       | `\Aabc` matches "abc" at the start |
| `\z`              | End of string                                         | `xyz\z` matches "xyz" at the end   |
| `\s`              | Any whitespace character                             | `\s+` matches one or more spaces   |
| `\S`              | Any non-whitespace character                         | `\S+` matches one or more non-spaces |
| `\d`              | Any digit                                             | `\d{3}` matches three digits       |
| `\D`              | Any non-digit                                         | `\D+` matches one or more non-digits |
| `\w`              | Any word character (letter, number, underscore)      | `\w+` matches one or more word characters |
| `\W`              | Any non-word character                                | `\W` matches any non-word character |
| `\b`              | Word boundary                                         | `\bword\b` matches whole word "word" |
| `(?i)`            | Case-insensitive flag                                 | `(?i)abc` matches "abc" case-insensitive |
| `(?m)`            | Multiline mode flag                                   | `(?m)^line` matches "line" at the start of each line |
| `(?x)`            | Ignore whitespace and allow comments in regex         | `(?x)a b c` matches "abc" ignoring spaces |
| `(?o)`            | Perform #{...} substitutions only once               | `(?o)#{variable}` substitutes variable once |


## Resources

interactive exercises on https://regexone.com/ 

more on regexp http://immike.net/blog/2007/04/06/the-absolute-bare-minimum-every-programmer-should-know-about-regular-expressions/
