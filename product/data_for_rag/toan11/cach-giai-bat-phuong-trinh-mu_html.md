# Cách giải bất phương trình mũ

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
Bài viết hướng dẫn giải một số dạng toán bất phương trình mũ thường gặp trong chương trình Giải tích 12.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## A. TÓM TẮT SÁCH GIÁO KHOA

Bất phương trình mũ cơ bản là bất phương trình có một trong các dạng:

${a^x} > m$, ${a^x} \ge m$, ${a^x} < m$, ${a^x} \le m$ với $0 < a \ne 1.$

** B. PHƯƠNG PHÁP GIẢI TOÁN**

**Phương pháp chung:**

Áp dụng tính chất đồng biến, nghịch biến của hàm số mũ để giải.

<!-- chunk:2 level:2 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Vấn đề 1: Bất phương trình mũ dạng cơ bản.

1. PHƯƠNG PHÁP: 

Với bất phương trình ${a^x} > m$ $(1).$

+ Nếu $m \le 0$ thì tập nghiệm của $(1)$ là $S = R$ (vì ${a^x} > 0$, $\forall x \in R$).

+ Nếu $m>0$ thì: 
$$
(1) \Leftrightarrow \left[ {\begin{array}{l}
{x > {{\log }_a}m{\rm{\:khi\:}}a > 1}\\
{x < {{\log }_a}m{\rm{\:khi\:}}0 < a < 1}
\end{array}} \right..
$$

2. CÁC VÍ DỤ:

<!-- chunk:3 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Ví dụ 1: Giải các bất phương trình sau:

a) ${3^x} > 81.$

b) ${\left( {\frac{1}{2}} \right)^x} > 32.$

a) ${3^x} > 81$ $\Leftrightarrow {3^x} > {3^4}$ $\Leftrightarrow x > 4.$

b) ${\left( {\frac{1}{2}} \right)^x} > 32$ $\Leftrightarrow {\left( {\frac{1}{2}} \right)^x} > {2^5}$ $\Leftrightarrow {2^{ – x}} > {2^5}$ $\Leftrightarrow – x > 5$ $\Leftrightarrow x < – 5.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Ví dụ 2: Giải bất phương trình sau: ${3^x} + {3^{x + 1}} + {3^{x – 1}} < {5^x} + {5^{x + 1}} + {5^{x – 1}}.$

Ta có: ${3^x} + {3^{x + 1}} + {3^{x – 1}} < {5^x} + {5^{x + 1}} + {5^{x – 1}}$ $\Leftrightarrow {3^x}\left( {1 + 3 + \frac{1}{3}} \right) < {5^x}\left( {1 + 5 + \frac{1}{5}} \right)$ $\Leftrightarrow {\left( {\frac{3}{5}} \right)^x} < \frac{{93}}{{65}}$ $\Leftrightarrow x > {\log _{\frac{3}{5}}}\frac{{93}}{{65}}.$

## Bài tập

## Bài tập 1. Giải các bất phương trình sau:

a) ${3^{{x^2} – 2x + {{\log }_3}5}} > 5.$

b) ${8.4^{\frac{{x – 3}}{{{x^2} + 1}}}} < 1.$

## Bài tập 2. Giải các bất phương trình:

a) ${2^{ – {x^2} + 3x}} < 4.$

b) ${\left( {\frac{7}{9}} \right)^{2{x^2} – 3x}} \ge \frac{9}{7}.$

## Bài tập 3. Giải bất phương trình: ${3^{x + 2}} + {3^{x – 1}} \le 28.$

## Bài tập 4. Giải bất phương trình: ${5^{{{\log }_3}\frac{{x – 2}}{x}}} < 1.$

<!-- chunk:5 level:2 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Vấn đề 2: Đưa bất phương trình mũ về cùng một cơ số.
1. PHƯƠNG PHÁP:

Với $0 < a \ne 1$. Ta có:

+ ${a^{f(x)}} > {a^{g(x)}}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{f(x) > g(x)\:nếu\:a > 1}\\
{f(x) < g(x)\:nếu\:0 < a < 1}
\end{array}} \right..
$$

+ ${a^{f(x)}} \ge {a^{g(x)}}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{f(x) \ge g(x)\:nếu\:a > 1}\\
{f(x) \le g(x)\:nếu\:0 < a < 1}
\end{array}} \right..
$$

2. CÁC VÍ DỤ:

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Ví dụ 1: Giải bất phương trình: ${3^{{x^2} – 2x}} < 3.$

Ta có: ${3^{{x^2} – 2x}} < 3$ $\Leftrightarrow {x^2} – 2x < 1$ $\Leftrightarrow 1 – \sqrt 2 < x < 1 + \sqrt 2 .$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Ví dụ 2: Giải bất phương trình: ${2^{|x – 2|}} > {4^{|x + 1|}}.$

Ta có: ${2^{|x – 2|}} > {4^{|x + 1|}}$ $\Leftrightarrow {2^{|x – 2|}} > {2^{2|x + 1|}}$ $\Leftrightarrow |x – 2| > 2|x + 1|$ $\Leftrightarrow {x^2} – 4x + 4 > 4{x^2} + 8x + 4$ $\Leftrightarrow 3{x^2} + 12x < 0$ $\Leftrightarrow – 4 < x < 0.$

Vậy nghiệm của bất phương trình là: $-4< x < 0.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Ví dụ 3: Giải bất phương trình: ${\left( {\sqrt {10} + 3} \right)^{\frac{{x – 3}}{{x – 1}}}} < {\left( {\sqrt {10} – 3} \right)^{\frac{{x + 1}}{{x + 3}}}}.$

Điều kiện: $x \ne 1$, $x \ne – 3.$

Nhận xét: $(\sqrt {10} + 3).(\sqrt {10} – 3) = 1$ $\Rightarrow (\sqrt {10} – 3) = {(\sqrt {10} + 3)^{ – 1}}.$

${(\sqrt {10} + 3)^{\frac{{x – 3}}{{x – 1}}}} < {(\sqrt {10} – 3)^{\frac{{x + 1}}{{x + 3}}}}$ $\Leftrightarrow {(\sqrt {10} + 3)^{\frac{{x – 3}}{{x – 1}}}} < {(\sqrt {10} + 3)^{ – \frac{{x + 1}}{{x + 3}}}}$ $\Leftrightarrow \frac{{x – 3}}{{x – 1}} < – \frac{{x + 1}}{{x + 3}}$ $\Leftrightarrow \frac{{x – 3}}{{x – 1}} + \frac{{x + 1}}{{x + 3}} < 0$ $\Leftrightarrow \frac{{{x^2} – 5}}{{(x – 1)(x + 3)}} < 0$ $\Leftrightarrow – 3 < x < – \sqrt 5$ hoặc $1 < x < \sqrt 5 .$

Vậy nghiệm của bất phương trình: $– 3 < x < – \sqrt 5$ hoặc $1 < x < \sqrt 5 .$

## Bài tập

## Bài tập 1. Giải bất phương trình: ${(\sqrt 2 + 1)^{\frac{{6x – 6}}{{x + 1}}}} \le {(\sqrt 2 – 1)^{ – x}}.$

## Bài tập 2. Giải các bất phương trình sau:

a) $\frac{1}{{{2^{|2x – 1|}}}} > \frac{1}{{{2^{3x – 1}}}}.$

b) ${\left( {\frac{3}{7}} \right)^{{x^2} + 1}} \ge {\left( {\frac{3}{7}} \right)^{3x – 1}}.$

## Bài tập 3. Giải bất phương trình: ${3^{\sqrt {{x^2} – 2x} }} \ge {\left( {\frac{1}{3}} \right)^{x – |x – 1|}}.$

## Bài tập 4. Giải bất phương trình: ${x^{2{x^2} – 5x + 2}} \ge 1$ (với $0 < x \ne 1$).

<!-- chunk:9 level:2 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Vấn đề 3: Phương pháp đặt ẩn số phụ.

1. PHƯƠNG PHÁP: 

Nếu đặt $t = {a^x}$, điều kiện $t>0$ thì:

${a^{2x}} = {\left( {{a^2}} \right)^x} = {\left( {{a^x}} \right)^2} = {t^2}.$

${a^{3x}} = {t^3}.$

${a^{ – x}} = \frac{1}{t}.$

……

Lưu ý một số kết quả sau thường sử dụng khi đặt ẩn phụ:

${(\sqrt 2 – 1)^x}{(\sqrt 2 + 1)^x} = 1.$

${(2 – \sqrt 3 )^x}{(2 + \sqrt 3 )^x} = 1.$

${(4 – \sqrt {15} )^x}{(4 + \sqrt {15} )^x} = 1.$

${(\sqrt {7 – \sqrt {48} } )^x}{(\sqrt {7 + \sqrt {48} } )^x} = 1.$

2. CÁC VÍ DỤ:

<!-- chunk:10 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Ví dụ 1: Giải bất phương trình: ${4^x} – {2.5^{2x}} < {10^x}.$

${4^x} – {2.5^{2x}} < {10^x}$ $\Leftrightarrow 1 – 2.{\left( {\frac{5}{2}} \right)^{2x}} < {\left( {\frac{5}{2}} \right)^x}$ $(1).$

Đặt $t = {\left( {\frac{5}{2}} \right)^x}$, điều kiện $t > 0.$

$(1)$ trở thành $1 – 2{t^2} < t$ $\Leftrightarrow 2{t^2} + t – 1 > 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t < – 1}\\
{t > \frac{1}{2}}
\end{array}} \right.
$$
 $\Leftrightarrow {\left( {\frac{5}{2}} \right)^x} > \frac{1}{2}$ $\Leftrightarrow x > {\log _{\frac{5}{2}}}\frac{1}{2}$ $\Leftrightarrow x > – {\log _{\frac{5}{2}}}2.$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Ví dụ 2: Giải bất phương trình: ${(\sqrt 5 + 1)^{x – {x^2}}} + {2^{ – {x^2} + x + 1}} < 3.{(\sqrt 5 – 1)^{x – {x^2}}}.$

Ta có: ${(\sqrt 5 + 1)^{x – {x^2}}} + {2^{ – {x^2} + x + 1}} < 3.{(\sqrt 5 – 1)^{x – {x^2}}}$ $(1).$

Ta có: ${2^{ – {x^2} + x}} > 0$ với mọi $x.$ Chia hai vế cho ${2^{ – {x^2} + x}}$ ta được:

$(1) \Leftrightarrow {\left( {\frac{{\sqrt 5 + 1}}{2}} \right)^{x – {x^2}}} + 2 < 3{\left( {\frac{{\sqrt 5 – 1}}{2}} \right)^{x – {x^2}}}$ $(2).$

Ta nhận thấy $\left( {\frac{{\sqrt 5 + 1}}{2}} \right)\left( {\frac{{\sqrt 5 – 1}}{2}} \right) = 1.$

Đặt ${\left( {\frac{{\sqrt 5 + 1}}{2}} \right)^{x – {x^2}}} = t$, $t > 0$ $\Rightarrow {\left( {\frac{{\sqrt 5 – 1}}{2}} \right)^{x – {x^2}}} = \frac{1}{t}.$

$(2)$ trở thành:

$t + 2 < \frac{3}{t}$ $\Leftrightarrow {t^2} + 2t – 3 < 0$ $\Leftrightarrow 0 < t < 1$ $\Leftrightarrow 0 < {\left( {\frac{{\sqrt 5 + 1}}{2}} \right)^{x – {x^2}}} < 1$ $\Leftrightarrow x – {x^2} < 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x < 0}\\
{x > 1}
\end{array}} \right..
$$

## Bài tập

## Bài tập 1. Giải các bất phương trình sau:

a) ${4^x} – {3.2^x} + 2 > 0.$

b) ${\left( {\frac{1}{3}} \right)^{\frac{2}{x}}} + {\left( {\frac{1}{3}} \right)^{\frac{1}{x}}} > 12.$

## Bài tập 2. Giải các bất phương trình sau:

a) ${9^{\sqrt {{x^2} – 3x} }} + 3 < {28.3^{\sqrt {{x^2} – 3x – 1} }}.$

b) ${2^{3x}} – \frac{8}{{{2^{3x}}}} – 6\left( {{2^x} – \frac{1}{{{2^{x – 1}}}}} \right) \le 1.$

## Bài tập 3. Giải bất phương trình: ${25^{1 + 2x – {x^2}}} + {9^{1 + 2x – {x^2}}} \ge {34.15^{2x – {x^2}}}.$

## Bài tập 4. Giải các bất phương trình sau:

a) ${3^{2x}} – {8.3^{x + \sqrt {x + 4} }} – {9.9^{\sqrt {x + 4} }} > 0.$

b) ${2^{2\sqrt {x + 3} – x – 6}} + {15.2^{\sqrt {x + 3} – 5}} < {2^x}.$

## Bài tập 5. Giải bất phương trình: ${x^2}{2^{2x}} + 9(x + 2){.2^x} + 8{x^2}$ $\le (x + 2){2^{2x}} + 9{x^2}{2^x} + 8x + 16.$

<!-- chunk:12 level:2 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Vấn đề 4: Phương pháp lôgarit hóa.

1. PHƯƠNG PHÁP: 

Với bất phương trình mũ mà hai vế là tích hay thương của nhiều lũy thừa với các cơ số khác nhau thì ta có thể lấy lôgarit hai vế, ta có:

+ ${a^{f(x)}} > {b^{g(x)}}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{f(x) > g(x).{{\log }_a}b{\rm{\:nếu\:}}a > 1}\\
{f(x) < g(x).{{\log }_a}b{\rm{\:nếu\:}}0 < a < 1}
\end{array}.} \right.
$$

+ ${a^{f(x)}} \ge {b^{g(x)}}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{f(x) \ge g(x).{{\log }_a}b{\rm{\:nếu\:}}a > 1}\\
{f(x) \le g(x).{{\log }_a}b{\rm{\:nếu\:}}0 < a < 1}
\end{array}.} \right.
$$

2. CÁC VÍ DỤ:

<!-- chunk:13 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Ví dụ 1: Giải bất phương trình: ${3^{2x – 1}} < {11^{3 – x}}.$

${3^{2x – 1}} < {11^{3 – x}}$ $\Leftrightarrow 2x – 1 < {\log _3}{11^{3 – x}}$ $\Leftrightarrow 2x – 1 < (3 – x){\log _3}11$ $\Leftrightarrow x < \frac{{3{{\log }_3}11 + 1}}{{2 + {{\log }_3}11}}.$

<!-- chunk:14 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-mu.html -->
## Ví dụ 2: Giải bất phương trình ${(x – 2)^{{x^2} – 6x + 8}} > 1$ với $2 < x \ne 3.$

${(x – 2)^{{x^2} – 6x + 8}} > 1$ với $2 < x \ne 3$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x – 2 > 0}\\
{(x – 2 – 1)\left( {{x^2} – 6x + 8 – 0} \right) > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x > 2}\\
{2 < x < 3{\rm{\:hoặc\:}}x > 4}
\end{array}} \right.
$$
 $\Leftrightarrow 2 < x < 3$ hoặc $x > 4.$

## Bài tập

## Bài tập 1. Giải các bất phương trình sau:

a) ${5^{{x^2} – 1}} + {5^{{x^2}}} \ge {7^x} – {7^{x – 1}}.$

b) ${5^{4{x^2} – 3}} > {5.3^{3x – 3}}.$

## Bài tập 2. Giải các bất phương trình sau:

a) ${5^x}{.8^{\frac{{x – 1}}{x}}} > 500.$

b) ${3^{{x^2}}}{.2^x} \le 1.$