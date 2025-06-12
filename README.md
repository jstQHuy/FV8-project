# FV8-project
``python
┌──(kali㉿kali)-[~/Desktop]
└─$ echo -ne '\x02\x08\x66\x6c\x61\x67\x2e\x74\x78\x74'|nc -u chals.swampctf.com 44254
swampCTF{r3v3r53_my_pr070_l1k3_m070_m070}
```
- `-ne` không xuống dòng và bật chế độ interpret backslash escapes - ví dụ hiểu được `\x02`
- `-u` netcat gửi qua phương thức udp

Flag: `swampCTF{r3v3r53_my_pr070_l1k3_m070_m070}`
