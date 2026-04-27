# Tìm nguyên hàm bằng phương pháp đổi biến số

<!-- chunk:0 level:0 source:https://toanmath.com/2018/04/tim-nguyen-ham-bang-phuong-phap-doi-bien-so.html -->
Bài viết hướng dẫn tìm nguyên hàm bằng phương pháp đổi biến số. Kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu nguyên hàm – tích phân và ứng dụng được đăng tải trên TOANMATH.com.

Phương pháp đổi biến số để xác định nguyên hàm có hai dạng dựa trên định lý sau:

Định lý:

a/ Nếu $\int {f(x)dx = F(x) + C}$ và $u = \varphi (x)$ là hàm số có đạo hàm thì $\int {f(u)du = F(u) + C}.$

b/ Nếu hàm số $f(x)$ liên tục thì khi đặt $x = \varphi (t)$ trong đó $\varphi (t)$ cùng với đạo hàm của nó ($\varphi'(t)$) là những hàm số liên tục, ta sẽ được: $\int {f(x)dx = \int {f\left[ {\varphi (t)} \right]} .\varphi'(t)dt} .$

Từ đó ta trình bày hai bài toán về phương pháp đổi biến như sau:

<!-- chunk:1 level:2 source:https://toanmath.com/2018/04/tim-nguyen-ham-bang-phuong-phap-doi-bien-so.html -->
## Bài toán 1: Sử dụng phương pháp đổi biến số dạng 1 tìm nguyên hàm $I = \int {f(x)dx}$

PHƯƠNG PHÁP CHUNG

Ta thực hiện theo các bước:

+ Bước 1: Chọn $x = \varphi (t)$, trong đó $\varphi (t)$ là hàm số mà ta chọn cho thích hợp.

+ Bước 2: Lấy vi phân $dx = \varphi'(t)dt.$

+ Bước 3: Biểu thị $f(x)dx$ theo $t$ và $dt.$ Giả sử rằng $f(x)dx = g(t)dt.$

+ Bước 4: Khi đó $I = \int {g(t)dt} .$

Lưu ý: Các dấu hiệu dẫn tới việc lựa chọn ẩn phụ kiểu trên thông thường là:

+ Dấu hiệu $\sqrt {{a^2} – {x^2}}$, đặt $x = |a|\sin t$ với $\frac{{ – \pi }}{2} \le t \le \frac{\pi }{2}$ hoặc $x = |a|\cos t$ với $0 \le t \le \pi .$

+ Dấu hiệu $\sqrt {{x^2} – {a^2}}$, đặt $x = \frac{{|a|}}{{\sin t}}$ với $t \in \left[ { – \frac{\pi }{2};\frac{\pi }{2}} \right]\backslash \left\{ 0 \right\}$ hoặc $x = \frac{{|a|}}{{\cos t}}$ với $t \in \left[ {0;\pi } \right]\backslash \left\{ {\frac{\pi }{2}} \right\}.$

+ Dấu hiệu $\sqrt {{a^2} + {x^2}}$, đặt $x = |a|\tan t$ với $– \frac{\pi }{2} < t < \frac{\pi }{2}$ hoặc $x = |a|\cot t$ với $0 < t < \pi .$

+ Dấu hiệu $\sqrt {\frac{{a + x}}{{a – x}}}$ hoặc $\sqrt {\frac{{a – x}}{{a + x}}}$, đặt $x = a\cos 2t.$

+ Dấu hiệu $\sqrt {(x – a)(b – x)}$, đặt $x = a + (b – a){\sin ^2}t.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/04/tim-nguyen-ham-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 1: Tìm nguyên hàm $I = \int {\frac{{dx}}{{\sqrt {{{(1 – {x^2})}^3}} }}} .$

Đặt $x = sint$; $– \frac{\pi }{2} < t < \frac{\pi }{2}.$

Suy ra: $dx = \cos tdt$ và $\frac{{dx}}{{\sqrt {{{(1 – {x^2})}^3}} }} = \frac{{\cos tdt}}{{{{\cos }^3}t}}$ $= \frac{{dt}}{{{{\cos }^2}t}} = d(\tan t).$

Khi đó: $I = \int {d(\tan t) = \tan t + C}$ ${ = \frac{x}{{\sqrt {1 – {x^2}} }} + C}.$

Chú ý: Trong ví dụ trên sở dĩ ta có: $\sqrt {{{(1 – {x^2})}^3}} = {\cos ^3}t$ và $\tan t = \frac{x}{{\sqrt {1 – {x^2}} }}$ là bởi: $– \frac{\pi }{2} < t < \frac{\pi }{2} \Rightarrow \cos t > 0$ $\Rightarrow \sqrt {{{\cos }^2}t} = \cos t$ và $\cos t = \sqrt {1 – {{\sin }^2}t} = \sqrt {1 – {x^2}} .$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/04/tim-nguyen-ham-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 2: Tìm nguyên hàm $I = \int {\frac{{{x^2}dx}}{{\sqrt {{x^2} – 1} }}} .$

Vì điều kiện $|x| > 1$, ta xét hai trường hợp:

+ Với $x > 1$:

Đặt $x = \frac{1}{{\sin 2t}}$; $0 < t < \frac{\pi }{4}.$

Suy ra:

$dx = \frac{{2\cos 2tdt}}{{{{\sin }^2}2t}}.$

$\frac{{{x^2}dx}}{{\sqrt {{x^2} – 1} }} = – \frac{{2dt}}{{{{\sin }^3}2t}}$ $= – \frac{{2{{(co{s^2}t + {{\sin }^2}t)}^2}dt}}{{8{{\sin }^3}t{{\cos }^3}t}}$

$= – \frac{1}{4}(\cot t.\frac{1}{{{{\sin }^2}t}}$ $+ \tan t.\frac{1}{{{{\cos }^2}t}} + \frac{2}{{\tan t}}.\frac{2}{{{{\cos }^2}t}})$

$= – \frac{1}{4}[ – \cot t.d(\cot t)$ $+ \tan t.d(\tan t) + 2\frac{{d(\tan t)}}{{\tan t}}].$

Khi đó: $I = – \frac{1}{4}[ – \int {\cot t.d(\cot t)}$ $+ \int {\tan t.d(\tan t)} + 2\int {\frac{{d(\tan t)}}{{\tan t}}} ]$

$= – \frac{1}{4}( – \frac{1}{2}{\cot ^2}t + \frac{1}{2}{\tan ^2}t$ $+ 2\ln |\tan t|) + C$

$= \frac{1}{8}\left( {{{\cot }^2}t – {{\tan }^2}t} \right)$ $– \frac{1}{2}\ln |\tan t| + C$

$= \frac{1}{2}x\sqrt {{x^2} – 1}$ $– \frac{1}{2}\ln |x – {x^2} – 1| + C.$

+ Với $x < –1$: Bạn đọc biến đổi tương tự.

Chú ý: Trong ví dụ trên sở dĩ ta có: ${\cot ^2}t – {\tan ^2}t = 4x\sqrt {{x^2} – 1}$ và $\tan t = x – \sqrt {{x^2} – 1}$ là bởi:

${\cot ^2}t – {\tan ^2}t = \frac{{{{\cos }^4}t – {{\sin }^4}t}}{{{{\cos }^2}t.{{\sin }^2}t}}$ $= \frac{{4\cos 2t}}{{{{\sin }^2}2t}} = \frac{{4\sqrt {1 – {{\sin }^2}2t} }}{{{{\sin }^2}2t}}$ $= \frac{4}{{\sin 2t}}\sqrt {\frac{1}{{{{\sin }^2}2t}} – 1} .$

$\tan t = \frac{{\sin t}}{{\cos t}}$ $= \frac{{2{{\sin }^2}t}}{{2\sin t.\cos t}} = \frac{{1 – \cos 2t}}{{\sin 2t}}$ $= \frac{1}{{\sin 2t}} – \sqrt {\frac{{{{\cos }^2}2t}}{{{{\sin }^2}2t}}}$ $= \frac{1}{{\sin 2t}} – \sqrt {\frac{1}{{{{\sin }^2}2t}} – 1} .$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/04/tim-nguyen-ham-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 3: Tìm nguyên hàm $I = \int {\frac{{dx}}{{\sqrt {{{(1 + {x^2})}^3}} }}} .$

Đặt $x = tant$; $– \frac{\pi }{2} < t < \frac{\pi }{2}.$

Suy ra:

$dx = \frac{{dt}}{{{{\cos }^2}t}}.$

$\frac{{dx}}{{\sqrt {{{(1 + {x^2})}^3}} }}$ $= \frac{{{{\cos }^3}tdt}}{{{{\cos }^2}t}} = \cos tdt.$

Khi đó: $I = \int {\cos tdt = \sin t + C}$ ${ = \frac{x}{{\sqrt {1 + {x^2}} }} + C}.$

Chú ý:

1. Trong ví dụ trên sở dĩ ta có: $\frac{1}{{\sqrt {1 + {x^2}} }} = \cos t$ và $\sin t = \frac{x}{{\sqrt {1 + {x^2}} }}$ là bởi: $– \frac{\pi }{2} < t < \frac{\pi }{2} \Rightarrow \cos t > 0$ 
$$
\Rightarrow \left\{ \begin{array}{l}
\sqrt {{{\cos }^2}t} = \cos t\\
\sin t = \tan t.\cos t = \frac{x}{{\sqrt {1 + {x^2}} }}
\end{array} \right.
$$

2. Phương pháp trên được áp dụng để giải bài toán tổng quát: $I = \int {\frac{{dx}}{{\sqrt {{{\left( {{a^2} + {x^2}} \right)}^{2k + 1}}} }}}$ với $k ∈ Z.$

[ads]

<!-- chunk:5 level:2 source:https://toanmath.com/2018/04/tim-nguyen-ham-bang-phuong-phap-doi-bien-so.html -->
## Bài toán 2: Sử dụng phương pháp đổi biến số dạng 2 tìm nguyên hàm $I = \int {f(x)dx}$

PHƯƠNG PHÁP CHUNG
Ta thực hiện theo các bước:

+ Bước 1: Chọn $t = \psi (x)$, trong đó $\psi (x)$ là hàm số mà ta chọn cho thích hợp.

+ Bước 2: Xác định vi phân $dt = \psi'(x)dx.$

+ Bước 3: Biểu thị $f(x)dx$ theo $t$ và $dt.$ Giả sử rằng $f(x)dx = g(t)dt.$

+ Bước 4: Khi đó $I = \int {g(t)dt.}$

Lưu ý: Các dấu hiệu dẫn tới việc lựa chọn ẩn phụ kiểu trên thông thường là:

+ Dấu hiệu $f(x,\sqrt {\varphi (x)} )$, đặt $t = \sqrt {\varphi (x)} .$

+ Dấu hiệu $f(x) = \frac{{a.\sin x + b.\cos x}}{{c.\sin x + d.\cos x + e}}$, đặt $t = \tan \frac{x}{2}$ (với $\cos \frac{x}{2} \ne 0$).

+ Dấu hiệu $f(x) = \frac{1}{{\sqrt {(x + a)(x + b)} }}$: với $x + a > 0$ và $x + b > 0$, đặt $t = \sqrt {x + a} + \sqrt {x + b}$; với $x + a < 0$ và $x + b < 0$, đặt $t = \sqrt { – x – a} + \sqrt { – x – b} .$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/04/tim-nguyen-ham-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 4: Tìm nguyên hàm $I = \int {{x^3}{{\left( {2 – 3{x^2}} \right)}^8}dx} .$

Đặt 
$$
t = 2 – 3{x^2} \Rightarrow \left\{ \begin{array}{l}
dt = – 6xdx\\
{x^2} = \frac{{2 – t}}{3}
\end{array} \right.
$$

Khi đó: ${x^3}{\left( {2 – 3{x^2}} \right)^8}dx$ $= {x^2}{\left( {2 – 3{x^2}} \right)^8}xdx$ $= \frac{{2 – t}}{3}{t^8}\left( { – \frac{1}{6}dt} \right)$ $= \frac{1}{{18}}\left( {{t^9} – 2{t^8}} \right)dt.$

Nên: $I = \frac{1}{{18}}\int {\left( {{t^9} – 2{t^8}} \right)dt}$ ${ = \frac{1}{{180}}{t^{10}} – \frac{1}{{81}}{t^9} + C}.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/04/tim-nguyen-ham-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 5: Tìm nguyên hàm $I = \int {\frac{{{x^2}dx}}{{\sqrt {1 – x} }}} .$

Đặt $t = \sqrt {1 – x} \Rightarrow x = 1 – {t^2}.$

Suy ra:

$dx = – 2tdt.$

$\frac{{{x^2}dx}}{{\sqrt {1 – x} }} = \frac{{{{\left( {1 – {t^2}} \right)}^2}( – 2tdt)}}{t}$ $= – 2\left( {{t^4} – 2{t^2} + 1} \right)dt.$

Khi đó: $I = – 2\int {\left( {{t^4} – 2{t^2} + 1} \right)dt}$ $= – 2\left( {\frac{{{t^5}}}{5} – \frac{{2{t^3}}}{3} + t} \right) + C$ $= \frac{{ – 2}}{{15}}\left( {3{x^2} + 4x + 8} \right)\sqrt {1 – x} + C.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/04/tim-nguyen-ham-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 6: Tìm nguyên hàm $I = \int {{{\sin }^3}x\sqrt {\cos x} dx} .$

Đặt $t = \sqrt {\cos x} \Rightarrow {t^2} = \cos x.$

Suy ra:

$2tdt = – \sin xdx.$

${\sin ^3}x\sqrt {\cos x} dx$ $= {\sin ^2}x\sqrt {\cos x} \sin xdx$ $= \left( {1 – {{\cos }^2}x} \right)\sqrt {\cos x} \sin xdx$

$= (1 – {t^4})t( – 2tdt)$ $= (2{t^6} – 2{t^2})dt.$

Khi đó: $I = \int {(2{t^6} – 2{t^2})dt}$ $= \frac{{2{t^7}}}{7} – \frac{{2{t^3}}}{3} + C$ $= \frac{{2{{\left( {\sqrt {\cos x} } \right)}^7}}}{7} – \frac{{2{{\left( {\sqrt {\cos x} } \right)}^3}}}{3} + C.$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/04/tim-nguyen-ham-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 7: Tìm nguyên hàm $I = \int {\frac{{dx}}{{\sqrt {1 + {e^x}} }}} .$

Đặt $t = \sqrt {1 + {e^x}} \Rightarrow {t^2} = 1 + {e^x}.$

Suy ra:

$2tdt = {e^x}dx \Rightarrow dx = \frac{{2tdt}}{{{t^2} – 1}}.$

$\frac{{dx}}{{\sqrt {1 + {e^x}} }} = \frac{{2tdt}}{{t\left( {{t^2} – 1} \right)}}$ $= \frac{{2dt}}{{{t^2} – 1}} = \left( {\frac{1}{{t – 1}} – \frac{1}{{t + 1}}} \right)dt.$

Khi đó: $I = \int {\left( {\frac{1}{{t – 1}} – \frac{1}{{t + 1}}} \right)dt}$ $= \ln \left| {\frac{{t – 1}}{{t + 1}}} \right| + C$ $= \ln \left| {\frac{{\sqrt {1 + {e^x}} – 1}}{{\sqrt {1 + {e^x}} + 1}}} \right| + C.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/04/tim-nguyen-ham-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 8: Tìm nguyên hàm $I = \int {\frac{{dx}}{{\sqrt {{x^2} + a} }}}$, với $a ≠ 0.$

Đặt $t = x + \sqrt {{x^2} + a} .$

Suy ra: $dt = \left( {1 + \frac{x}{{\sqrt {{x^2} + a} }}} \right)dx$ $= \frac{{\sqrt {{x^2} + a} + x}}{{\sqrt {{x^2} + a} }}dx$ $\Leftrightarrow \frac{{dx}}{{\sqrt {{x^2} + a} }} = \frac{{dt}}{t}.$

Khi đó: $I = \int {\frac{{dt}}{t} = \ln \left| t \right|} + C$ $= \ln \left| {x + \sqrt {{x^2} + a} } \right| + C.$

<!-- chunk:11 level:3 source:https://toanmath.com/2018/04/tim-nguyen-ham-bang-phuong-phap-doi-bien-so.html -->
## Ví dụ 9: Tìm nguyên hàm $\int {\frac{{dx}}{{\sqrt {\left( {x + 1} \right)\left( {x + 2} \right)} }}} .$

Ta xét hai trường hợp:

+ Với 
$$
\left\{ \begin{array}{l}
x + 1 > 0\\
x + 2 > 0
\end{array} \right. \Leftrightarrow x > – 1.
$$

Đặt $t = \sqrt {x + 1} + \sqrt {x + 2} .$

Suy ra: $dt = \left( {\frac{1}{{2\sqrt {x + 1} }} + \frac{1}{{2\sqrt {x + 2} }}} \right)dx$ $= \frac{{\left( {\sqrt {x + 1} + \sqrt {x + 2} } \right)dx}}{{2\sqrt {(x + 1)(x + 2)} }}$

$\Leftrightarrow \frac{{dx}}{{\sqrt {(x + 1)(x + 2)} }} = \frac{{2dt}}{t}.$

Khi đó: $I = 2\int {\frac{{dt}}{t} = 2\ln \left| t \right| + C}$ ${ = 2\ln \left| {\sqrt {x + 1} + \sqrt {x + 2} } \right|} + C.$

+ 
$$
\left\{ \begin{array}{l}
x + 1 < 0\\
x + 2 < 0
\end{array} \right. \Leftrightarrow x < – 2.
$$

Đặt $t = \sqrt { – \left( {x + 1} \right)} + \sqrt { – \left( {x + 2} \right)} .$

Suy ra: $\Leftrightarrow \frac{{dx}}{{\sqrt {(x + 1)(x + 2)} }} = – \frac{{2dt}}{t}.$

Khi đó: $I = – 2\int {\frac{{dt}}{t} = – 2\ln \left| t \right|} + C$ $= – 2\ln \left| {\sqrt { – \left( {x + 1} \right)} + \sqrt { – \left( {x + 2} \right)} } \right| + C.$