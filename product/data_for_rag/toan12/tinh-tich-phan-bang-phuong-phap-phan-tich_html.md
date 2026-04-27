# Tính tích phân bằng phương pháp phân tích

<!-- chunk:0 level:0 source:https://toanmath.com/2018/05/tinh-tich-phan-bang-phuong-phap-phan-tich.html -->
Bài viết hướng dẫn tính tích phân bằng phương pháp phân tích. Kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu nguyên hàm – tích phân và ứng dụng được đăng tải trên TOANMATH.com.

Phương pháp:

Để tính tích phân $I = \int\limits_a^b {f(x)dx}$ ta phân tích $f(x) = {k_1}{f_1}(x) + … + {k_m}{f_m}(x)$, trong đó các hàm ${f_i}(x){\rm{ }}(i = 1,2,3,…,n)$ có trong bảng nguyên hàm.

<!-- chunk:1 level:3 source:https://toanmath.com/2018/05/tinh-tich-phan-bang-phuong-phap-phan-tich.html -->
## Ví dụ 1. Tính các tích phân sau:

1. $I = \int\limits_0^1 {\frac{{xdx}}{{\sqrt {3x + 1} + \sqrt {2x + 1} }}} .$

2. $J = \int\limits_2^7 {\frac{{xdx}}{{\sqrt {x + 2} + \sqrt {x – 2} }}} .$

1. Ta có: $x = (3x + 1) – (2x + 1)$ $= (\sqrt {3x + 1} – \sqrt {2x + 1} )(\sqrt {3x + 1} + \sqrt {2x + 1} ).$

Nên $I = \int\limits_0^1 {(\sqrt {3x + 1} – \sqrt {2x + 1} )dx}$ $= \left. {\left[ {\frac{2}{9}\sqrt {{{(3x + 1)}^3}} – \frac{1}{3}\sqrt {{{(2x + 1)}^3}} } \right]} \right|_0^1$ $= \frac{{17 – 9\sqrt 3 }}{9}.$

2. Ta có $x$ $= \frac{1}{4}(\sqrt {x + 2} + \sqrt {x – 2} )(\sqrt {x + 2} – \sqrt {x – 2} ).$

Nên $J = \frac{1}{4}\int\limits_2^7 {\left( {\sqrt {x + 2} – \sqrt {x – 2} } \right)dx}$ $= \frac{{19 – 5\sqrt 5 }}{6}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/05/tinh-tich-phan-bang-phuong-phap-phan-tich.html -->
## Ví dụ 2. Tính các tích phân sau:

1. $I = \int\limits_{ – \frac{\pi }{2}}^{\frac{\pi }{2}} {\sin 2x.\sin 3x} {\rm{ }}.$

2. $J = \int\limits_0^{\frac{\pi }{4}} {{{\cos }^4}2x} dx.$

1. Ta có: $I = \frac{1}{2}\int\limits_{ – \frac{\pi }{2}}^{\frac{\pi }{2}} {(\cos x – \cos 5x)dx}$ $= \left. {\frac{1}{2}(\sin x – \frac{1}{5}\sin 5x)} \right|_{ – \frac{\pi }{2}}^{\frac{\pi }{2}}$ $= \frac{4}{5}.$

2. Ta có: ${\cos ^4}2x$ $= \frac{1}{2}(1 + 2\cos 4x + {\cos ^2}4x)$ $= \frac{1}{4}(3 + 4\cos 4x + \cos 8x).$

Nên $J = \frac{1}{4}\int\limits_0^{\frac{\pi }{4}} {(3 + 4\cos 4x + \cos 8x)dx}$ $= \frac{1}{4}\left. {\left( {3x + \sin 4x + \frac{1}{8}\sin 8x} \right)} \right|_0^{\frac{\pi }{4}}$ $= \frac{{3\pi }}{{16}}.$

[ads]

<!-- chunk:3 level:3 source:https://toanmath.com/2018/05/tinh-tich-phan-bang-phuong-phap-phan-tich.html -->
## Ví dụ 3. Tính các tích phân sau:

1. $I = \int\limits_3^4 {\frac{{{x^2}dx}}{{{x^2} – 3x + 2}}} .$

2. $J = \int\limits_2^3 {\frac{{2x + 3}}{{{x^3} – 3x + 2}}dx} .$

1. Ta có: $\frac{{{x^2}}}{{{x^2} – 3x + 2}}$ $= 1 + \frac{3}{2}\frac{{2x – 3}}{{{x^2} – 3x + 2}}$ $+ \frac{5}{2}\frac{1}{{{x^2} – 3x + 2}}$ $= 1 + \frac{3}{2}\frac{{2x – 3}}{{{x^2} – 3x + 2}}$ $+ \frac{5}{2}\left( {\frac{1}{{x – 2}} – \frac{1}{{x – 1}}} \right).$

Suy ra: $I =$ $\left. {\left( {x + \frac{3}{2}ln\left| {{x^2} – 3x + 2} \right| + \frac{5}{2}\ln \left| {\frac{{x – 2}}{{x – 1}}} \right|} \right){\rm{ }}} \right|_3^4$ $= 1 + \frac{3}{2}\ln 3 + \frac{5}{2}\ln \frac{4}{3}.$

2. Ta có: ${x^3} – 3x + 2$ $= {(x – 1)^2}(x + 2)$

$2x + 3 = a{(x – 1)^2}$ $+ b(x + 2)(x – 1) + c(x + 2)$

$\Leftrightarrow 2x + 3 = (a + b){x^2}$ $+ (c – 2a + b)x + a – 2b + 2c$

$$
\Leftrightarrow \left\{ \begin{array}{l}
a + b = 0\\
– 2a + b + c = 2\\
a – 2b + 2c = 3
\end{array} \right.
$$
 $\Leftrightarrow a = – \frac{1}{9},b = \frac{1}{9},c = \frac{5}{3}.$

$J =$ $\int\limits_2^3 {\left[ { – \frac{1}{9}\frac{1}{{x + 2}} + \frac{1}{9}\frac{1}{{x – 1}} + \frac{5}{3}\frac{1}{{{{(x – 1)}^2}}}} \right]dx}$ $= \left. {\left( {\frac{1}{9}\ln \left| {\frac{{x – 1}}{{x + 2}}} \right| – \frac{5}{{3(x – 1)}}} \right){\rm{ }}} \right|_2^3$ $= \frac{1}{9}\ln \frac{8}{5} + \frac{5}{6}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/05/tinh-tich-phan-bang-phuong-phap-phan-tich.html -->
## Ví dụ 4. Tính các tích phân sau: $I = \int\limits_0^1 {x\left| {x – a} \right|dx} ,a > 0.$

Xét hai trường hợp:

$\bullet$ $a \ge 1$ $\Rightarrow I = \int\limits_0^1 {x(a – x)dx}$ $= \frac{{3a – 2}}{6}.$

$\bullet$ $0 < a < 1$ $\Rightarrow I = \int\limits_0^a {x(a – x)dx} + \int\limits_a^1 {x(x – a)dx}$ $= \frac{{2{a^3} – 3a + 2}}{6}.$