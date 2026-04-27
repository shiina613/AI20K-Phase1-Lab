# Ứng dụng số phức giải toán khai triển, tính tổng nhị thức Niutơn

<!-- chunk:0 level:0 source:https://toanmath.com/2018/04/ung-dung-so-phuc-giai-toan-khai-trien-tinh-tong-nhi-thuc-niuton.html -->
Bài viết giới thiệu phương pháp ứng dụng số phức giải toán khai triển, tính tổng nhị thức Niutơn, đây là lớp bài toán tương đối phức tạp đối với học sinh khối 11 khi các em giải toán bằng các phương pháp khác, tuy nhiên nếu biết áp dụng số phức (được học ở chương trình Giải tích 12) thì lời giải các bài toán sẽ trở nên gọn gàng và dễ hiểu hơn.

Phương pháp

Ta nhắc lại công thức khai triển nhị thức Niutơn:

${\left( {a + b} \right)^n} = \sum\limits_{k = 0}^n {C_n^k} {a^{n – k}}{b^k}$ $= C_n^o{a^n} + C_n^1{a^{n – 1}}b + C_n^1{a^{n – 2}}{b^2}$ $+ … + C_n^{n – 1}a{b^{n – 1}} + C_n^n{b^n}.$

Ta lưu ý rằng $\forall m \in {N^*}$ thì ${i^{4m}} = 1$, ${i^{4m + 1}} = i$, ${i^{4m + 2}} = – 1$, ${i^{4m + 3}} = – i.$

Các ví dụ điển hình thường gặp

<!-- chunk:1 level:3 source:https://toanmath.com/2018/04/ung-dung-so-phuc-giai-toan-khai-trien-tinh-tong-nhi-thuc-niuton.html -->
## Ví dụ 1. Tính tổng:

a. ${S_1} = 1 – C_n^2 + C_n^4 – C_n^6 + … .$

b. ${S_2} = C_n^1 – C_n^3 + C_n^5 – C_n^7 + … .$

Ta có:

${\left( {1 + i} \right)^n}$ $= 1 + C_n^1i + C_n^2{i^2} + … + C_n^n{i^n}$

$= \left( {1 – C_n^2 + C_n^4 – C_n^6 + …} \right)$ $+ i\left( {C_n^1 – C_n^3 + C_n^5 – C_n^7 + …} \right) (1).$

${\left( {1 + i} \right)^n}$ $= \sqrt {{2^n}} c{\rm{os}}\frac{{n\pi }}{4} + i\sqrt {{2^n}} {\rm{sin}}\frac{{n\pi }}{4} (2).$

Từ $(1)$ và $(2)$ suy ra:

${{\rm{S}}_1} = \sqrt {{2^n}} c{\rm{os}}\frac{{n\pi }}{4}.$

${S_2} = \sqrt {{2^n}} {\rm{sin}}\frac{{n\pi }}{4}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/04/ung-dung-so-phuc-giai-toan-khai-trien-tinh-tong-nhi-thuc-niuton.html -->
## Ví dụ 2. Chứng minh rằng: $C_{100}^0 – C_{100}^2 + C_{100}^4 – C_{100}^6$ $+ … – C_{100}^{98} + C_{100}^{100} = – {2^{50}}.$

${\left( {1 + i} \right)^{100}}$ $= C_{100}^0 + C_{100}^1i + C_{100}^2{i^2} + … + C_{100}^{100}{i^{100}}$

$= \left( {C_{100}^0 – C_{100}^2 + C_{100}^4 – … + C_{100}^{100}} \right)$ $+ \left( {C_{100}^1 – C_{100}^3 + C_{100}^5 + … – C_{100}^{99}} \right)i.$

${\left( {1 + i} \right)^2} = 2i$ $\Rightarrow {\left( {1 + i} \right)^{100}} = {\left( {2i} \right)^{50}} = – {2^{50}}.$

Vậy: $C_{100}^0 – C_{100}^2 + C_{100}^4 – … + C_{100}^{100} = – {2^{50}}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/04/ung-dung-so-phuc-giai-toan-khai-trien-tinh-tong-nhi-thuc-niuton.html -->
## Ví dụ 3. Tính các tổng sau:

$A = C_{15}^0 – 3C_{15}^2 + 5C_{15}^4 – 7C_{15}^6$ $+ …. + 13C_{15}^{12} – 15C_{15}^{14}.$

$B = 2C_{15}^1 – 4C_{15}^3 + 6C_{15}^5 – 8C_{15}^7$ $+ …. + 14C_{15}^{13} – 16C_{15}^{15}.$

Xét khai triển:

${\left( {1 + x} \right)^{15}}$ $= C_{15}^0 + C_{15}^1x + C_{15}^2{x^2} + C_{15}^3{x^3}$ $+ … + C_{15}^{12}{x^{12}} + C_{15}^{13}{x^{13}} + C_{15}^{14}{x^{14}} + C_{15}^{15}{x^{15}}$

$\Rightarrow x{\left( {1 + x} \right)^{15}}$ $= C_{15}^0x + C_{15}^1{x^2} + C_{15}^2{x^3} + C_{15}^3{x^4}$ $+ … + C_{15}^{12}{x^{13}} + C_{15}^{13}{x^{14}} + C_{15}^{14}{x^{15}} + C_{15}^{15}{x^{16}}.$

Lấy đạo hàm hai vế:

${\left( {1 + x} \right)^{15}} + 15x{\left( {1 + x} \right)^{14}}$

$= C_{15}^0 + 2C_{15}^1x + 3C_{15}^2{x^2} + 4C_{15}^3{x^3}$ $+ … + 13C_{15}^{12}{x^{12}} + 14C_{15}^{13}{x^{13}}$ $+ 15C_{15}^{14}{x^{14}} + 16C_{15}^{15}{x^{15}}.$

Thay $x$ bởi $i$ ta được:

${\left( {1 + i} \right)^{15}} + 15i{\left( {1 + i} \right)^{14}}$ $= C_{15}^0 + 2C_{15}^1i + 3C_{15}^2{i^2} + 4C_{15}^3{i^3}$ $+ … + 13C_{15}^{12}{i^{12}} + 14C_{15}^{13}{i^{13}}$ $+ 15C_{15}^{14}{i^{14}} + 16C_{15}^{15}{i^{15}}$

= (${C_{15}^0 – 3C_{15}^2 + 5C_{15}^4 – 7C_{15}^6}$ ${ + …. + 13C_{15}^{12} – 15C_{15}^{14}}$) + (${2C_{15}^1 – 4C_{15}^3 + 6C_{15}^5 – 8C_{15}^7}$ ${ + …. + 14C_{15}^{13} – 16C_{15}^{15}}$)$i.$

Mặt khác:

${\left( {1 + i} \right)^{15}} + 15i{\left( {1 + i} \right)^{14}}$ $= \sqrt {{2^{15}}} {\left( {c{\rm{os}}\frac{\pi }{4} + {\rm{i}}\sin \frac{\pi }{4}} \right)^{15}}$ $+ 15i\sqrt {{2^{14}}} {\left( {c{\rm{os}}\frac{\pi }{4} + {\rm{i}}\sin \frac{\pi }{4}} \right)^{14}}$

$= \sqrt {{2^{15}}} \left( {\frac{{\sqrt 2 }}{2} – \frac{{\sqrt 2 }}{2}i} \right) + 15i{.2^7}\left( { – i} \right)$ $= {2^7} – {2^7}i + {15.2^7}$ $= {16.2^7} – {2^7}i = {2^{11}} – {2^7}i.$

Vậy:

$A = C_{15}^0 – 3C_{15}^2 + 5C_{15}^4 – 7C_{15}^6$ $+ …. + 13C_{15}^{12} – 15C_{15}^{14} = {2^{11}}.$

$B = 2C_{15}^1 – 4C_{15}^3 + 6C_{15}^5 – 8C_{15}^7$ $+ …. + 14C_{15}^{13} – 16C_{15}^{15} = – {2^7}.$

[ads]

<!-- chunk:4 level:3 source:https://toanmath.com/2018/04/ung-dung-so-phuc-giai-toan-khai-trien-tinh-tong-nhi-thuc-niuton.html -->
## Ví dụ 4. Chứng minh rằng:

${S_1} = C_n^0 – C_n^2 + C_n^4 – C_n^6 + C_n^8 – …$ $= {\left( {\sqrt 2 } \right)^n}\cos \frac{{n\pi }}{4}.$

${S_2} = C_n^1 – C_n^3 + C_n^5 – C_n^7 + C_n^9 – …$ $= {\left( {\sqrt 2 } \right)^n}\sin \frac{{n\pi }}{4}.$

Xét khai triển nhị thức Newton:

${\left( {1 + i} \right)^n}$ $= C_n^0 + iC_n^1 + {i^2}C_n^2 + {i^3}C_n^3 + {i^4}C_n^4$ $+ … + {i^{n – 1}}C_n^{n – 1} + {i^n}C_n^n.$

Vì 
$$
{i^k} = \left\{ \begin{array}{l}
1, (k = 4m)\\
i, (k = 4m + 1)\\
– 1, (k = 4m + 2)\\
– i, (k = 4m + 3)
\end{array} \right.
$$
 với $m \in {{\rm Z}^ + }$, nên ta có:

${\left( {1 + i} \right)^n}$ $= C_n^0 – C_n^2 + C_n^4 – …$ $+ i\left( {C_n^1 – C_n^3 + C_n^5 – ….} \right).$

Mặt khác, theo công thức Moivre thì:

${\left( {1 + i} \right)^n}$ $= {\left( {\sqrt 2 } \right)^n}{\left( {\cos \frac{\pi }{4} + i\sin \frac{\pi }{4}} \right)^n}$ $= {\left( {\sqrt 2 } \right)^n}\left( {\cos \frac{{n\pi }}{4} + i\sin \frac{{n\pi }}{4}} \right).$

Từ $(1)$ và $(2)$ ta có điều phải chứng minh.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/04/ung-dung-so-phuc-giai-toan-khai-trien-tinh-tong-nhi-thuc-niuton.html -->
## Ví dụ 5. Tính tổng $S = \frac{1}{2}C_{2n}^1 – \frac{1}{4}C_{2n}^3 + \frac{1}{6}C_{2n}^5 – \frac{1}{8}C_{2n}^7 + …$

Chú ý rằng $\frac{1}{{2k}}C_{2n}^{2k – 1} = \frac{1}{{2n + 1}}C_{2n + 1}^{2k}$ nên:

$S = \frac{1}{2}C_{2n}^1 – \frac{1}{4}C_{2n}^3 + \frac{1}{6}C_{2n}^5 – \frac{1}{8}C_{2n}^7 + …$

$= \frac{1}{{2n + 1}}C_{2n + 1}^2 – \frac{1}{{2n + 1}}C_{2n + 1}^4$ $+ \frac{1}{{2n + 1}}C_{2n + 1}^6 – \frac{1}{{2n + 1}}C_{2n + 1}^8 + …$

$= \frac{1}{{2n + 1}}$.$\left( {C_{2n + 1}^2 – C_{2n + 1}^4 + C_{2n + 1}^6 – C_{2n + 1}^8 + …} \right).$

Vì ${\left( {1 + i} \right)^{2n + 1}}$ $= \left( {C_{2n + 1}^0 – C_{2n + 1}^2 + C_{2n + 1}^4 – …} \right)$ $+ i\left( {C_{2n + 1}^1 – C_{2n + 1}^3 + C_{2n + 1}^5 – …} \right).$

Và ${\left( {1 + i} \right)^{2n + 1}}$ $= {\left( {\sqrt 2 } \right)^{2n + 1}}$ $\left( {\cos \frac{{2n + 1}}{4}\pi + i\sin \frac{{2n + 1}}{4}\pi } \right)$ nên:

$C_{2n + 1}^0 – C_{2n + 1}^2 + C_{2n + 1}^4 – C_{2n + 1}^6$ $+ … = {\left( {\sqrt 2 } \right)^{2n + 1}}\cos \frac{{2n + 1}}{4}\pi .$

Vậy ta có $S = \frac{1}{{2n + 1}}$ $\left[ {1 – {{\left( {\sqrt 2 } \right)}^{2n + 1}}\cos \frac{{2n + 1}}{4}\pi } \right].$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/04/ung-dung-so-phuc-giai-toan-khai-trien-tinh-tong-nhi-thuc-niuton.html -->
## Ví dụ 6. Tính tổng: $(n \in {{\rm Z}^ + }).$

$A = C_n^0\cos a + C_n^1\cos 2a + C_n^2\cos 3a$ $+ … + C_n^{n – 1}\cos na + C_n^n\cos (n + 1)a.$

$B = C_n^0\sin a + C_n^1\sin 2a + C_n^2\sin 3a$ $+ … + C_n^{n – 1}\sin na + C_n^n\sin (n + 1)a.$

Đặt $z = \cos a + i\sin a$ thì ${z^n} = \cos na + i\sin na.$

Do đó ta có:

$A + iB = C_n^0\left( {\cos a + i\sin a} \right)$ $+ C_n^1\left( {\cos 2a + i\sin 2a} \right)$ $+ C_n^2\left( {\cos 3a + i\sin 3a} \right)$

$+ … + C_n^{n – 1}\left( {\cos na + i\sin na} \right)$ $+ C_n^n\left( {\cos (n + 1)a + i\sin (n + 1)a} \right)$

$= z\left( {C_n^0 + C_n^1z + C_n^2{z^2} + C_n^3{z^3} + … + C_n^n{z^n}} \right)$ $= z{\left( {1 + z} \right)^n}.$

Vì $1 + z = 1 + \cos a + i\sin a$ $= 2\cos \frac{a}{2}\left( {\cos \frac{a}{2} + i\sin \frac{a}{2}} \right).$

Nên: $A + iB = \left( {\cos a + i\sin a} \right)$.${\left[ {2\cos \frac{a}{2}\left( {\cos \frac{a}{2} = i\sin \frac{a}{2}} \right)} \right]^n}$

$= {2^n}{\cos ^n}\frac{a}{2}\left( {\cos a + i\sin a} \right)$.$\left( {\cos \frac{{na}}{2} + i\sin \frac{{na}}{2}} \right)$

$= {2^n}{\cos ^n}\frac{a}{2}$.$\left( {\cos \frac{{n + 2}}{2}a + i\sin \frac{{n + 2}}{2}a} \right)$

Vậy $A = {2^n}{\cos ^n}\frac{a}{2}\cos \frac{{n + 2}}{2}a$, $B = {2^n}{\cos ^n}\frac{a}{2}\sin \frac{{n + 2}}{2}a.$

Nhận xét: Cho $n$ là giá trị cụ thể, suy ra được nhiều biểu thức lượng giác đẹp.

Ví dụ: $\cos a + 5\cos 2a + 10\cos 3a$ $+ 10\cos 4a + 5\cos 5a + \cos 6a$ $= {2^5}{\cos ^5}\frac{a}{2}\cos \frac{{7a}}{2}.$