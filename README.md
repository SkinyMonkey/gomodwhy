# gomodwhy
A script to trace the reason why a project depends on a go module

The current go mod why subcommand seems broken and I could never use it.

It will show you a tree of import, from the module which imports needs to be explained
to the module that originally imports it

# usage

You can copy gomodwhy to /usr/local/bin or any directory that's in your $PATH.

Then from your project directory do:

```go mod graph | gomodwhy KEYWORDS```

Where keywords are module names, module with versions, with hash etc etc
If multiple module match that name a tree of import will be printed for each

Example:

```
crates $> go mod graph | gomodgraph purell
github.com/PuerkitoBio/purell@v1.1.0
 github.com/go-openapi/spec@v0.18.0
	 github.com/SkinyMonkey/crates
```
