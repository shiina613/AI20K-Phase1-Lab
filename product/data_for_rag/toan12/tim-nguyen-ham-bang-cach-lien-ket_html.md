# Tìm nguyên hàm bằng cách liên kết

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/tim-nguyen-ham-bang-cach-lien-ket.html -->
Bài viết hướng dẫn phương pháp tìm nguyên hàm bằng cách liên kết, giúp học sinh học tốt chương trình Giải tích 12: Nguyên hàm, Tích phân và Ứng dụng.

<!-- chunk:1 level:1 source:https://toanmath.com/2020/03/tim-nguyen-ham-bang-cach-lien-ket.html -->
## A. KIẾN THỨC CƠ BẢN

Giả sử cần lấy nguyên hàm của hàm số $f(x)$ mà gặp khó khăn. Nếu tìm được một hàm số $g(x)$ sao cho có thể lấy nguyên hàm của các hàm số $f(x) + g(x)$ và $f(x) – g(x)$, thì ta sẽ lấy hai nguyên hàm này và bằng cách giải hệ phương trình sẽ suy ra nguyên hàm của $f(x).$

** B. CÁC DẠNG TOÁN ĐIỂN HÌNH

****DẠNG 1. LIÊN KẾT CÁC HÀM LƯỢNG GIÁC.**

**1. ****Phương pháp**:

+ Chọn hàm liên kết thích hợp.

+ Tìm nguyên hàm của tổng và hiệu các hàm liên kết.

+ Giải hệ phương trình để xác định nguyên hàm cần tìm.

2. Ví dụ minh họa:

<!-- chunk:2 level:3 source:https://toanmath.com/2020/03/tim-nguyen-ham-bang-cach-lien-ket.html -->
## Ví dụ 1. Cho $I = \int {\frac{{\sin xdx}}{{\sin x + \cos x}}}$ và $J = \int {\frac{{\cos xdx}}{{\sin x + \cos x}}} .$ Tính $I + J$ và $I – J.$ Suy ra giá trị của $I$ và $J$?

Lời giải:

$I + J$ $= \int {\frac{{\sin x + \cos x}}{{\sin x + \cos x}}dx}$ $= \int {1.dx} = x + {C_1}.$

$I – J$ $= \int {\frac{{\sin x – \cos x}}{{\cos x + \sin x}}dx}$ $= \int {\frac{{ – (\cos x + \sin x)’}}{{\cos x + \sin x}}dx}$ $= – \ln |\cos x + \sin x| + {C_2}.$

$\Rightarrow 2I$ $= x – \ln |\cos x + \sin x|$ $+ {C_1} + {C_2}.$

$2J$ $= x + \ln |\cos x + \sin x|$ $+ {C_1} – {C_2}.$

Vậy: $I = \frac{1}{2}\left[ {x – \ln |\cos x + \sin x|} \right] + C.$

$J = \frac{1}{2}\left[ {x + \ln |\cos x + \sin x|} \right] + C.$

<!-- chunk:3 level:3 source:https://toanmath.com/2020/03/tim-nguyen-ham-bang-cach-lien-ket.html -->
## Ví dụ 2. Tính: $I = \int {{{\cos }^2}} x\cos 2xdx$ và $J = \int {{{\sin }^2}} x\cos 2xdx.$

Lời giải:

Ta có:

$I + J$ $= \int {\cos 2xdx}$ $= \frac{1}{2}\sin 2x + {C_1}$ $(1).$

$I – J$ $= \int {\left( {{{\cos }^2}x – {{\sin }^2}x} \right)} \cos 2xdx$ $= \int {{{\cos }^2}} 2xdx.$

$I – J$ $= \frac{1}{2}\int {(1 + \cos 4x)dx}$ $= \frac{1}{2}\left( {x + \frac{1}{4}\sin 4x} \right) + {C_2}$ $(2).$

Từ $(1)$ và $(2)$ suy ra 
$$
\left\{ {\begin{array}{l}
{I + J = \frac{1}{2}\sin 2x + {C_1}\,\,\,(1)}\\
{I – J = \frac{1}{2}\left( {x + \frac{1}{4}\sin 4x} \right) + {C_2}\,\,\,(2)}
\end{array}} \right..
$$

$$
\Rightarrow \left\{ {\begin{array}{l}
{I = \frac{1}{4}\left( {x + \sin 2x + \frac{1}{4}\sin 4x} \right) + C}\\
{J = – \frac{1}{4}\left( {x – \sin 2x + \frac{1}{4}\sin 4x} \right) + C}
\end{array}} \right..
$$

<!-- chunk:4 level:3 source:https://toanmath.com/2020/03/tim-nguyen-ham-bang-cach-lien-ket.html -->
## Ví dụ 3. Tính $I = \int {\frac{{{{\cos }^2}x}}{{\cos 2x}}dx} .$

Lời giải:

Đặt $J = \int {\frac{{{{\sin }^2}x}}{{\cos 2x}}dx.}$

Ta có: $I + J$ $= \int {\left( {\frac{{{{\cos }^2}x}}{{\cos 2x}} + \frac{{{{\sin }^2}x}}{{\cos 2x}}} \right)dx}$ $= \int {\frac{1}{{\cos 2x}}dx.}$

$= \frac{1}{2}\ln \left| {\tan \left( {x + \frac{\pi }{4}} \right)} \right| + {C_1}.$

$I – J$ $= \int {\frac{{{{\cos }^2}x – {{\sin }^2}x}}{{\cos 2x}}dx}$ $= \int {\frac{{\cos 2x}}{{\cos 2x}}dx}$ $= \int {1dx}$ $= x + {C_2}.$

Suy ra: $2I$ $= x + \frac{1}{2}\ln \left| {\tan \left( {x + \frac{\pi }{4}} \right)} \right|$ $+ {C_1} + {C_2}.$

Vậy $I = \frac{x}{2} + \frac{1}{4}\ln \left| {\tan \left( {x + \frac{\pi }{4}} \right)} \right| + C.$

**DẠNG 2. LIÊN KẾT HÀM MŨ VÀ LÔGARÍT.**

**1. Phương pháp**: Sử dụng phương pháp lấy nguyên hàm từng phần kết hợp với phương pháp liên kết.

2. Ví dụ minh họa:

<!-- chunk:5 level:3 source:https://toanmath.com/2020/03/tim-nguyen-ham-bang-cach-lien-ket.html -->
## Ví dụ 1. Tính: $I = \int {{e^{ax}}.\cos bxdx}$ và $J = \int {{e^{ax}}.\sin bxdx.}$

Lời giải:

Tính $I:$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = {e^{ax}}\quad \Rightarrow u’ = a.{e^x}}\\
{v’ = \cos bx \Rightarrow v = \frac{1}{b}\sin bx}
\end{array}} \right..
$$

$\Rightarrow I = \frac{1}{b}{e^{ax}}.\sin bx – \frac{a}{b}\int {{e^{ax}}\sin bxdx} .$

$= \frac{1}{b}{e^{ax}}.\sin bx – \frac{a}{b}.J$ $(1).$

Tính $J:$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = {e^{ax}}\quad \Rightarrow u’ = a.{e^{ax}}}\\
{v’ = \sin bx \Rightarrow v = – \frac{1}{b}\cos bx}
\end{array}} \right..
$$

$\Rightarrow J = – \frac{1}{b}{e^{ax}}.\cos bx + \frac{a}{b}\int {{e^{ax}}.\cos bxdx} .$

$= – \frac{1}{b}{e^{ax}}.\cos bx + \frac{a}{b}.I$ $(2).$

Thay $(2)$ vào $(1):$ $I = \frac{1}{b}{e^{ax}}.\sin bx$ $– \frac{a}{b}\left( { – \frac{1}{b}{e^{ax}}\cos bx + \frac{a}{b}I} \right).$

Vậy $I = \frac{{{e^{ax}}(a\cos bx + b\sin bx)}}{{{a^2} + {b^2}}} + C.$

Tương tự thay $(1)$ vào $(2)$ ta được: $J = \frac{{{e^{ax}}(a\sin bx – b\cos bx)}}{{{a^2} + {b^2}}} + C.$

<!-- chunk:6 level:3 source:https://toanmath.com/2020/03/tim-nguyen-ham-bang-cach-lien-ket.html -->
## Ví dụ 2. Cho $I = \int {\frac{{{e^x}dx}}{{{e^x} + {e^{ – x}}}}}$ và $J = \int {\frac{{{e^{ – x}}dx}}{{{e^x} + {e^{ – x}}}}} .$ Tính $I + J$ và $I – J.$ Suy ra giá trị của $I$ và $J.$

Lời giải:

Ta có: $I + J$ $= \int {\left( {\frac{{{e^x}}}{{{e^x} + {e^{ – x}}}} + \frac{{{e^{ – x}}}}{{{e^x} + {e^{ – x}}}}} \right)dx}$ $= \int {1.dx} = x + {C_1}.$

$I – J$ $= \int {\left( {\frac{{{e^x}}}{{{e^x} + {e^{ – x}}}} – \frac{{{e^{ – x}}}}{{{e^x} + {e^{ – x}}}}} \right)dx} .$

$= \int {\frac{{{e^x} – {e^{ – x}}}}{{{e^x} + {e^{ – x}}}}dx}$ $= \int {\frac{{\left( {{e^x} + {e^{ – x}}} \right)’}}{{{e^x} + {e^{ – x}}}}dx} .$

$= \ln \left( {{e^x} + {e^{ – x}}} \right) + {C_2}.$

$\Rightarrow 2I = x + \ln \left( {{e^x} + {e^{ – x}}} \right) + {C_1} + {C_2}.$

$2J = x – \ln \left( {{e^x} + {e^{ – x}}} \right) + {C_1} – {C_2}.$

Vậy:

$I = \frac{1}{2}\left[ {x + \ln \left( {{e^x} + {e^{ – x}}} \right)} \right] + C.$

$J = \frac{1}{2}\left[ {x – \ln \left( {{e^x} + {e^{ – x}}} \right)} \right] + C’.$

<!-- chunk:7 level:3 source:https://toanmath.com/2020/03/tim-nguyen-ham-bang-cach-lien-ket.html -->
## Ví dụ 3. Tính: $I = \int {\cos (\ln x)dx}$ và $J = \int {\sin (\ln x)dx} .$

Lời giải:

Để tính $I = \int {\cos (\ln x)dx}$ ta dùng phương pháp tích phân từng phần bằng cách đặt 
$$
\left\{ {\begin{array}{l}
{u = \cos (\ln x) \Rightarrow du = – \frac{{\sin (\ln x)}}{x}dx}\\
{dv = dx\quad \Rightarrow v = x}
\end{array}} \right..
$$

Ta có: $I = \int {\cos (\ln x)dx}$ $= x\cos (\ln x) + \int {\sin (\ln x)dx}$ $= x\cos (\ln x) + J$ $(1).$

Tương tự, bằng cách đặt: $u = \sin (\ln x)$ và $dv = dx$, ta lại tính được: $J = x\sin (\ln x) – I$ $(2).$

Từ $(1)$ và $(2):$

$$
\left\{ {\begin{array}{l}
{I = x\cos (\ln x) + J}\\
{J = x\sin (\ln x) – I}
\end{array}} \right.
$$
 
$$
\left\{ {\begin{array}{l}
{I = \frac{1}{2}x\left[ {\cos (\ln x) + \sin (\ln x)} \right] + {C_1}}\\
{J = \frac{1}{2}x\left[ {\sin (\ln x) – \cos (\ln x)} \right] + {C_2}}
\end{array}} \right..
$$

<!-- chunk:8 level:1 source:https://toanmath.com/2020/03/tim-nguyen-ham-bang-cach-lien-ket.html -->
## C. BÀI TOÁN TỰ LUYỆN

## Bài 1. Tìm nguyên hàm của hàm số: $f(x) = \frac{{{{\cos }^4}x}}{{{{\cos }^4}x + {{\sin }^4}x}}.$

## Bài 2. Tính $I = \int {\left( {a{{\cos }^2}wt + b{{\sin }^2}wt} \right)dt.}$

<!-- chunk:9 level:1 source:https://toanmath.com/2020/03/tim-nguyen-ham-bang-cach-lien-ket.html -->
## D. ĐÁP SỐ VÀ HƯỚNG DẪN GIẢI

## Bài 1. Với $g(x) = \frac{{{{\sin }^4}x}}{{{{\cos }^4}x + {{\sin }^4}x}}.$ Ta có: $f(x) + g(x) = 1.$

Và $f(x) – g(x)$ $= \frac{{{{\cos }^4}x – {{\sin }^4}x}}{{{{\cos }^4}x + {{\sin }^4}x}}$ $= \frac{{\cos 2x}}{{1 – \frac{1}{2}{{\sin }^2}2x}}.$

$= \frac{{2\cos 2x}}{{2 – {{\sin }^2}2x}}$ $= \frac{{(\sin 2x)’}}{{2 – {{\sin }^2}2x}}.$

Vậy 
$$
\left\{ {\begin{array}{l}
{F(x) + G(x) = x + {C_1}}\\
{F(x) – G(x) = \frac{1}{{2\sqrt 2 }}\ln \left| {\frac{{\sqrt 2 + \sin 2x}}{{\sqrt 2 – \sin 2x}}} \right| + {C_2}}
\end{array}} \right..
$$

$\Rightarrow F(x) = \frac{x}{2} + \frac{1}{{4\sqrt 2 }}\ln \left| {\frac{{\sqrt 2 + \sin 2x}}{{\sqrt 2 – \sin 2x}}} \right| + C.$

## Bài 2. Đặt $J = \int {\left( {b{{\cos }^2}wt + a{{\sin }^2}wt} \right)dt} .$ Ta có:

$I + J$ $= \int {(a + b)dt}$ $= (a + b)t + {C_1}$ $(1).$

$I – J$ $= \int {(a – b)} \cos 2wtdt$ $= \frac{{a – b}}{{2w}}\sin 2wt + {C_2}$ $(2).$

Từ $(1)$ và $(2)$ $\Rightarrow I = \frac{{a – b}}{{4w}}\sin 2wt$ $+ \frac{{a + b}}{2}t + C.$

Chú ý: Ta có thể tính trực tiếp $I$ bằng cách biến đổi:

${\cos ^2}wt = \frac{{1 + \cos 2wt}}{2}$ và ${\sin ^2}wt = \frac{{1 – \cos 2wt}}{2}$ rồi thay vào vẫn đạt được kết quả.