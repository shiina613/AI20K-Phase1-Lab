# Tìm nguyên hàm bằng phương pháp phân tích

<!-- chunk:0 level:0 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-phan-tich.html -->
Bài viết hướng dẫn tìm nguyên hàm bằng phương pháp phân tích. Kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu nguyên hàm – tích phân và ứng dụng được đăng tải trên TOANMATH.com.

Phương pháp: Để tìm nguyên hàm $\int {f(x)dx}$, ta phân tích:

$f(x) = {k_1}.{f_1}(x) + {k_2}.{f_2}(x) + … + {k_n}.{f_n}(x).$

Trong đó: ${f_1}(x), {f_2}(x), …, {f_n}(x)$ có trong bảng nguyên hàm hoặc ta dễ dàng tìm được nguyên hàm.

Khi đó: $\int {f(x)dx} = {k_1}\int {{f_1}(x)dx}$ $+ {k_2}\int {{f_2}(x)dx} + … + {k_n}\int {{f_n}(x)dx} .$

Ví dụ minh họa

<!-- chunk:1 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-phan-tich.html -->
## Ví dụ 1. Tìm nguyên hàm:

1. $I = \int {\frac{{2{x^2} + x + 1}}{{x – 1}}dx} .$

2. $J = \int {\frac{{{x^3} – 1}}{{x + 1}}dx} .$

3. $K = \int {{{\left( {x – \frac{1}{x}} \right)}^3}dx} .$

1. Ta có: $\frac{{2{x^2} + x + 1}}{{x – 1}}$ $= 2x + 3 + \frac{4}{{x – 1}}.$

Suy ra $I = \int {(2x + 3 + \frac{4}{{x – 1}})dx}$ $= {x^2} + 3x + 4\ln \left| {x – 1} \right| + C.$

2. Ta có: $\frac{{{x^3} – 1}}{{x + 1}} = \frac{{{x^3} + 1 – 2}}{{x + 1}}$ $= {x^2} – x + 1 – \frac{2}{{x + 1}}.$

Suy ra $J = \int {\left( {{x^2} – x + 1 – \frac{2}{{x + 1}}} \right)dx}$ $= \frac{{{x^3}}}{3} – \frac{{{x^2}}}{2} + x – 2\ln \left| {x + 1} \right| + C.$

3. Ta có: ${\left( {x – \frac{1}{x}} \right)^3}$ $= {x^3} – 3x + \frac{3}{x} – \frac{1}{{{x^3}}}.$

Suy ra $K = \int {\left( {{x^3} – 3x + \frac{3}{x} – \frac{1}{{{x^3}}}} \right)dx}$ $= \frac{{{x^4}}}{4} – \frac{{3{x^2}}}{2} + 3\ln \left| x \right| + \frac{1}{{2{x^2}}} + C.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-phan-tich.html -->
## Ví dụ 2. Tìm nguyên hàm:

1. $I = \int {\frac{{dx}}{{{{({x^2} – 1)}^2}}}} .$

2. $J = \int {\frac{{{x^3} + 2x + 1}}{{{x^2} + 2x + 1}}dx} .$

3. $K = \int {\frac{{2{x^2} + 1}}{{{{(x + 1)}^5}}}dx} .$

1. Ta có: $\frac{1}{{{{({x^2} – 1)}^2}}}$ $= \frac{1}{4}\frac{{{{\left[ {(x + 1) – (x – 1)} \right]}^2}}}{{{{\left[ {(x – 1)(x + 1)} \right]}^2}}}$

$= \frac{1}{4}\left[ {\frac{1}{{{{(x – 1)}^2}}} – \frac{2}{{(x – 1)(x + 1)}} + \frac{1}{{{{(x + 1)}^2}}}} \right]$ $= \frac{1}{4}\left[ {\frac{1}{{{{(x – 1)}^2}}} – \frac{1}{{x – 1}} + \frac{1}{{x + 1}} + \frac{1}{{{{(x + 1)}^2}}}} \right].$

Suy ra $I = \frac{1}{4}\left[ { – \frac{1}{{x – 1}} + \ln \left| {\frac{{x + 1}}{{x – 1}}} \right| – \frac{1}{{x + 1}}} \right] + C.$

2. Ta có: ${x^3} + 2x + 1$ $= {(x + 1)^3} – 3{(x + 1)^2}$ $+ 5(x + 1) – 2.$

Suy ra $J = \int {(x – 2 + \frac{5}{{x + 1}} – \frac{2}{{{{(x + 1)}^2}}})dx}$

$= \frac{{{x^2}}}{2} – 2x + 5\ln \left| {x + 1} \right| + \frac{2}{{x + 1}} + C.$

3. Ta phân tích $2{x^2} + 1$ $= 2{(x + 1)^2} – 4(x + 1) + 3.$

Suy ra:

$K = \int {\left( {\frac{2}{{{{(x + 1)}^3}}} – \frac{4}{{{{(x + 1)}^4}}} + \frac{3}{{{{(x + 1)}^5}}}} \right)dx}$

$= – \frac{1}{{{{(x + 1)}^2}}} + \frac{4}{{3{{(x + 1)}^3}}} – \frac{3}{{4{{(x + 1)}^4}}} + C.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-phan-tich.html -->
## Ví dụ 3. Tìm nguyên hàm:

1. $I = \int {{{({e^x} + 2{e^{ – x}})}^2}dx} .$

2. $J = \int {\frac{{{3^x} + {{4.5}^x}}}{{{7^x}}}dx} .$

1. Ta có: ${({e^x} + 2{e^{ – x}})^2}$ $= {e^{2x}} + 4 + 4.{e^{ – 2x}}.$

Suy ra: $I = \int {({e^{2x}} + 4 + 4{e^{ – 2x}})dx}$ $= \frac{1}{2}{e^{2x}} + 4x – 2{e^{ – 2x}} + C.$

2. $J = \int {\left( {{{\left( {\frac{3}{7}} \right)}^x} + 4.{{\left( {\frac{5}{7}} \right)}^x}} \right)dx}$ $= \frac{1}{{\ln \frac{3}{7}}}.{\left( {\frac{3}{7}} \right)^x} + \frac{4}{{\ln \frac{5}{7}}}.{\left( {\frac{5}{7}} \right)^x} + C.$

[ads]

<!-- chunk:4 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-phan-tich.html -->
## Ví dụ 4. Tìm nguyên hàm: $I = \int {\frac{{{{\sin }^4}x}}{{{{\cos }^2}x}}dx} .$

$I = \int {\left( {\frac{1}{{{{\cos }^2}x}} + {{\cos }^2}x – 2} \right)dx}$

$I = \tan x – 2x$ $+ \int {\frac{{dx}}{2}} + \frac{1}{4}\int {\cos 2xd\left( {2x} \right)}$ $= \tan x – \frac{3}{2}x + \frac{1}{4}\sin 2x + C.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-phan-tich.html -->
## Ví dụ 5. Tìm nguyên hàm:

1. $I = \int {{{\cos }^4}2xdx} .$

2. $J = \int {(\cos 3x.\cos 4x + {{\sin }^3}2x)dx} .$

1. Ta có: ${\cos ^4}2x = \frac{1}{4}{\left( {1 + \cos 4x} \right)^2}$ $= \frac{1}{4}\left( {1 + 2\cos 4x + {{\cos }^2}4x} \right)$

$= \frac{1}{4}\left( {1 + 2\cos 4x + \frac{{1 + \cos 8x}}{2}} \right)$ $= \frac{1}{8}\left( {3 + 4\cos 4x + \cos 8x} \right)$

$\Rightarrow I = \frac{1}{8}\int {(3 + 4\cos 4x + \cos 8x)dx}$ $= \frac{1}{8}\left( {3x + \sin 4x + \frac{1}{8}\sin 8x} \right) + C.$

2. Ta có: $\cos 3x.\cos 4x = \frac{1}{2}\left[ {\cos 7x + \cos x} \right].$

${\sin ^3}2x = \frac{3}{4}\sin 2x – \frac{1}{4}\sin 6x.$

Nên suy ra: $J = \frac{1}{{14}}\sin 7x + \frac{1}{2}\sin x$ $– \frac{3}{8}\cos 2x + \frac{1}{{24}}\cos 6x + C.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-phan-tich.html -->
## Ví dụ 6. Tìm nguyên hàm:

1. $I = \int {\left( {\frac{1}{{{{\ln }^2}x}} – \frac{1}{{\ln x}}} \right)dx} .$

2. $J = \int {\frac{{x{e^x} + 1}}{{{{(x + {e^x})}^2}}}dx} .$

1. Ta có: $\frac{1}{{{{\ln }^2}x}} – \frac{1}{{\ln x}} = \frac{{1 – \ln x}}{{{{\ln }^2}x}}$ $= \frac{{x(\ln x)’ – (x)’\ln x}}{{{{\ln }^2}x}} = \left( {\frac{x}{{\ln x}}} \right)’.$

Vậy $I = \int {\left( {\frac{x}{{\ln x}}} \right)’dx} = \frac{x}{{\ln x}} + C.$

2. Ta có: $\frac{{x{e^x} + 1}}{{{{(x + {e^x})}^2}}}$ $= – \frac{{(x + 1)'(x + {e^x}) – (x + {e^x})'(x + 1)}}{{{{(x + {e^x})}^2}}}$ $= – \left( {\frac{{x + 1}}{{x + {e^x}}}} \right)’.$

Suy ra $J = – \frac{{x + 1}}{{x + {e^x}}} + C.$