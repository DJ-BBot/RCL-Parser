# RCL Language Reference

## Token Definitions

RCL, as stated previously is a fairly simple configuration language.

There are several key tokens that should be observed:

`#`  - The `#` character represents a comment line which will be ignored by
the parser. All characters after the `#` token are ignored by the parser

`=>` - The `=>` arrow represents the beginning of a Symbol definition

`->` - The `->` arrow represents the beginning of a sub-symbol definition

`:`  - The `:` character represents a definition separator. A symbol can
have multiple values associated with it by using this character

`\`  - The `\` character will escape any Tokens

`\\` - The `\\` indicates an escaped line break, continue the current symbols
definition with the next line

`\\\` - `\\\` indicates inclusion of a blank line in the symbols value assignment

`{}` - The `{}` token would be populated by a previously defined Symbol. Using
this token, the parser will take the definition of the Symbol contained in the
`{}` and insert the Symbol definition at that point

`.`  - The `.` is a symbol accessor. If a symbol has sub-properties we can use
the `.` - the `.` accessor token is typically used with the `{}` token

`;`  - The `;` token represents the end of an rcl statement

## Symbol Definition

Symbols in RCL are simply case-insensitive alpha-numeric character strings.

The preferred method of defining a symbol is to use all-upper snake case.

```RCL
# The following snippet provides a series of example RCL statements

HELLO_WORLD_PARAM => Hello World; # Assigns HELLO_WORLD_PARAM symbol the value of "Hello World"

USER_NAME => FIRST -> Roger : LAST -> Barker; # Assigns the USER_NAME symbol the values of FIRST (a sub-symbol) which is Roger and LAST, Barker.

GREETING => {USER_NAME.FIRST} says\: \\ # Assign the first GREETING symbol the definition of USER_NAME.FIRST, escape the `:` token, and escape the line break.

I am continuing my greeting here.; # This line finishes the assignment of the GREETING symbol

INCLUDE_NEW_LINE => This value is going to include a new line. \\
\\\ # The \\\ is a special character that tells the parser to include a blank line in the value of this symbol
Finish the definition here.; # finish the assignment statement.  

```

## Additional language information

Blank lines and lines that start with the `#` token are ignored by the parser
entirely. If an RCL author needs to include a blank line in their Symbol
definition, they should use the `\` token at the first character in the line
followed immediately by escaping the new line (`\\`). This makes a blank line
look like `\\\` in the Symbols value definition.
