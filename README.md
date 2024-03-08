# RCL-Parser

## Author Information

- Roger Barker
- [E-mail Roger](mailto:pendletonroger@gmail.com)

## About

RCL (Roger's Configuration Language) is a simple markup language that allows
for the generation of configuration files that can be easily processed by
various applications.

This repository will hold the tools needed to parse RCL

## Use Cases

RCL is intended to enhance projects by providing a simple configuration syntax
with an even simpler parsing process that returns a usable object in the
developers software projects.

I have used it for several reasons

- [x] Template configurations for modification of docx, pdf, xlsx, and other filetypes
- [x] Default Parameter definition for pythonic applications
- [x] Configuration of back-end data properties for web-applications
- [x] Code execution & build management

## Initial Support

RCL Parser currently supports

- [x] Python

Future state will include:

- [ ] Java
- [ ] C#
- [ ] C++
- [ ] Go
- [ ] Rust

## Intent of RCL

RCL will have two major components supporting multiple target languages.

First, the RCL-Parser will be brought in as an importable developer package.
This will provide developers with the tools they need to parse RCL configuration
files.

Second, the RCL-Parser will be utilized in a translator that will allow
developers to quickly generate generic types/enums that can be utilized in
product development.
