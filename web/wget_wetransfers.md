# Download a file from WeTransfer using wget

1) Start the download as usual (I use Chrome)
2) Copy the actual URL in the download section of your browser
3) Use this command `wget --user-agent Mozilla/4.0 '<url>' -O output.zip`

## Create a cool command
Open
`$ vi ~/.bashrc`
and append the following line

```
alias weget='wget --user-agent Mozilla/4.0'
```

Sometimes it doesn't work, because you need to use a more realistic
user agent.

I like this
```
--user-agent= "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0"
```