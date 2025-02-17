# CCR Fulltext XML

The goal of this project is to provide full-text JATS XML from CCR latex files.

Status: Very early development

## Installation

Install latexml: (see [Offical documentation](https://math.nist.gov/~BMiller/LaTeXML/get.html) for more options)

```{sh}
sudo apt install latexml
```

## Usage

To run latexml to generate JATS

```{sh}
latexmlc --destination=pinda.xml --format=jats main
```

To run the latexml and postprossing, use:

```{sh}
# Python command to follow :D
```
