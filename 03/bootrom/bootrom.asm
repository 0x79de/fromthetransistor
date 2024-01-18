section .text
    org 0x7C00 ; Bootrom'un yüklenme adresi

    ; Başlangıç noktası
start:
    xor ax, ax  ; AX register'ını sıfırla
    mov ds, ax  ; DS register'ını sıfırla
    mov es, ax  ; ES register'ını sıfırla

    ; Seri portu başlat
    mov dx, 0x3F8   ; COM1 port adresi
    mov al, 0       ; Divisor Latch Access Bit (DLAB) temizle
    out dx, al      ; COM1 portuna yaz
    mov al, 115200  ; Seri iletişim hızı
    out dx, al      ; COM1 portuna yaz

    ; Mesajı yazdır
    mov si, message ; Mesaj adresini SI registerine yüke
    call print_string ; print_string fonksiyonunu çağır

    ; sonsuz döngü
    jmp $
    
print_string:
    ; DS:SI adresindeki null-terminated string'i ekrana yazdır
    mov ah, 0x0E ; Teletype serv,s çağrısı
    next_char:
        lodsb ; SI adresindeki karakteri AL registerine yükle ve SI bir arttır
        cmp al, 0 ; Karakter null ise döngüyü sonlandır
        je done
        int 0x10 ; Teletype servisini çağır
        jmp next_char
    done:
        ret

section .data
    message db 'Hello Bootrom!', 0 ; Null-terminated string

