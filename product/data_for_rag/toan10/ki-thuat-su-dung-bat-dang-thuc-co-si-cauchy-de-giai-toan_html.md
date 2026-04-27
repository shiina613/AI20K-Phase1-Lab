# Kĩ thuật sử dụng bất đẳng thức Cô-si (Cauchy) để giải toán

<!-- chunk:0 level:0 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
Bài viết hướng dẫn kĩ thuật sử bất đẳng thức Cô-si (Cauchy) (bất đẳng thức giữa trung bình cộng và trung bình nhân) để chứng minh bất đẳng thức và tìm giá trị lớn nhất, giá trị nhỏ nhất.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## A. BẤT ĐẲNG THỨC CÔ-SI (CAUCHY)
Bất đẳng thức Cô-si đối với hai số không âm: Cho $a\ge 0$, $b\ge \text{0}$, ta có $\frac{a+b}{2}\ge \sqrt{ab}$. Đẳng thức xảy ra khi và chỉ khi $a=b.$

Hệ quả:

+ Hai số dương có tổng không đổi thì tích lớn nhất khi hai số đó bằng nhau.

+ Hai số dương có tích không đổi thì tổng nhỏ nhất khi hai số đó bằng nhau.

Bất đẳng thức Cô-si đối với ba số không âm: Cho $a\ge 0$, $b\ge 0$, $c\ge 0$, ta có $\frac{a+b+c}{3}\ge \sqrt[3]{abc}$. Đẳng thức xảy ra khi và chỉ khi $a=b=c.$

Một số lưu ý khi sử dụng bất đẳng thức Cô-si:

+ Khi áp dụng bất đẳng thức Cô-si thì các số phải là những số không âm.

+ Bất đẳng thức Cô-si thường được áp dụng khi trong bất đẳng thức cần chứng minh có tổng và tích.

+ Điều kiện xảy ra dấu ‘$=$’ là các số bằng nhau.

+ Bất đẳng thức Cô-si còn có hình thức khác thường hay sử dụng như sau:

Đối với hai số: ${{x}^{2}}+{{y}^{2}}\ge 2xy$; ${{x}^{2}}+{{y}^{2}}\ge \frac{{{(x+y)}^{2}}}{2}$; $xy\le {{\left( \frac{x+y}{2} \right)}^{2}}.$

Đối với ba số: $abc\le \frac{{{a}^{3}}+{{b}^{3}}+{{c}^{3}}}{3}$, $abc\le {{\left( \frac{a+b+c}{3} \right)}^{3}}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 1. Cho $a$, $b$ là số dương thỏa mãn ${{a}^{2}}+{{b}^{2}}=2$. Chứng minh rằng:

a) $\left( \frac{a}{b}+\frac{b}{a} \right)\left( \frac{a}{{{b}^{2}}}+\frac{b}{{{a}^{2}}} \right)\ge 4.$

b) ${{\left( a+b \right)}^{5}}\ge 16ab\sqrt{\left( 1+{{a}^{2}} \right)\left( 1+{{b}^{2}} \right)}.$

a) Áp dụng bất đẳng thức Cô-si, ta có:

$\frac{a}{b}+\frac{b}{a}\ge 2\sqrt{\frac{a}{b}.\frac{b}{a}}=2.$

$\frac{a}{{{b}^{2}}}+\frac{b}{{{a}^{2}}}\ge 2\sqrt{\frac{a}{{{b}^{2}}}.\frac{b}{{{a}^{2}}}}=\frac{2}{\sqrt{ab}}.$

Suy ra $\left( \frac{a}{b}+\frac{b}{a} \right)\left( \frac{a}{{{b}^{2}}}+\frac{b}{{{a}^{2}}} \right)\ge \frac{4}{\sqrt{ab}}$ $(1).$

Mặt khác ta có $2={{a}^{2}}+{{b}^{2}}\ge 2\sqrt{{{a}^{2}}{{b}^{2}}}=2ab$ $\Rightarrow ab\le 1$ $(2).$

Từ $(1)$ và $(2)$ suy ra $\left( \frac{a}{b}+\frac{b}{a} \right)\left( \frac{a}{{{b}^{2}}}+\frac{b}{{{a}^{2}}} \right)\ge 4.$

Đẳng thức xảy ra khi và chỉ khi $a=b=1.$

b) Ta có ${{\left( a+b \right)}^{5}}$ $=\left( {{a}^{2}}+2ab+{{b}^{2}} \right)\left( {{a}^{3}}+3a{{b}^{2}}+3{{a}^{2}}b+{{b}^{3}} \right).$

Áp dụng bất đẳng thức Cô-si ta có:

${{a}^{2}}+2ab+{{b}^{2}}$ $\ge 2\sqrt{2ab\left( {{a}^{2}}+{{b}^{2}} \right)}=4\sqrt{ab}.$

$\left( {{a}^{3}}+3a{{b}^{2}} \right)+\left( 3{{a}^{2}}b+{{b}^{3}} \right)$ $\ge 2\sqrt{\left( {{a}^{3}}+3a{{b}^{2}} \right)\left( 3{{a}^{2}}b+{{b}^{3}} \right)}$ $=4\sqrt{ab\left( 1+{{b}^{2}} \right)\left( {{a}^{2}}+1 \right)}.$

Suy ra $\left( {{a}^{2}}+2ab+{{b}^{2}} \right)\left( {{a}^{3}}+3a{{b}^{2}}+3{{a}^{2}}b+{{b}^{3}} \right)$ $\ge 16ab\sqrt{\left( {{a}^{2}}+1 \right)\left( {{b}^{2}}+1 \right)}.$

Do đó ${{\left( a+b \right)}^{5}}$ $\ge 16ab\sqrt{\left( 1+{{a}^{2}} \right)\left( 1+{{b}^{2}} \right)}.$

Đẳng thức xảy ra khi và chỉ khi $a=b=1.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 2. Cho $a$, $b$, $c$ là các số dương. Chứng minh rằng:

a) $\left( a+\frac{1}{b} \right)\left( b+\frac{1}{c} \right)\left( c+\frac{1}{a} \right)\ge 8.$

b) ${{a}^{2}}(1+{{b}^{2}})+{{b}^{2}}(1+{{c}^{2}})+{{c}^{2}}(1+{{a}^{2}})\ge 6abc.$

c) $(1+a)(1+b)(1+c)\ge {{\left( 1+\sqrt[3]{abc} \right)}^{3}}.$

d) ${{a}^{2}}\sqrt{bc}+{{b}^{2}}\sqrt{ac}+{{c}^{2}}\sqrt{ab}$ $\le {{a}^{3}}+{{b}^{3}}+{{c}^{3}}.$

a) Áp dụng bất đẳng thức Cô-si ta có:

$a+\frac{1}{b}\ge 2\sqrt{\frac{a}{b}}.$

$b+\frac{1}{c}\ge 2\sqrt{\frac{b}{c}}.$

$c+\frac{1}{a}\ge 2\sqrt{\frac{c}{a}}.$

Suy ra $\left( a+\frac{1}{b} \right)\left( b+\frac{1}{c} \right)\left( c+\frac{1}{a} \right)$ $\ge 8\sqrt{\frac{a}{b}}.\sqrt{\frac{b}{c}}.\sqrt{\frac{c}{a}}=8.$

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$

b) Áp dụng bất đẳng thức Cô-si cho hai số dương, ta có:

$1+{{a}^{2}}\ge 2\sqrt{{{a}^{2}}}=2a.$

$1+{{b}^{2}}\ge 2b.$

$1+{{c}^{2}}\ge 2c.$

Suy ra ${{a}^{2}}(1+{{b}^{2}})+{{b}^{2}}(1+{{c}^{2}})+{{c}^{2}}(1+{{a}^{2}})$ $\ge 2\left( {{a}^{2}}b+{{b}^{2}}c+{{c}^{2}}a \right).$

Mặt khác, áp dụng bất đẳng thức Cô-si cho ba số dương, ta có:

${{a}^{2}}b+{{b}^{2}}c+{{c}^{2}}a$ $\ge 3\sqrt{{{a}^{2}}b.{{b}^{2}}c.{{c}^{2}}a}=3abc.$

Suy ra ${{a}^{2}}(1+{{b}^{2}})+{{b}^{2}}(1+{{c}^{2}})+{{c}^{2}}(1+{{a}^{2}})\ge 6abc$.

Đẳng thức xảy ra khi và chỉ khi $a=b=c=1.$

c) Ta có $(1+a)(1+b)(1+c)$ $=1+\left( ab+bc+ca \right)+\left( a+b+c \right)+abc.$

Áp dụng bất đẳng thức Cô-si cho ba số dương, ta có:

$ab+bc+ca$ $\ge 3\sqrt[3]{ab.bc.ca}=3{{\left( \sqrt[3]{abc} \right)}^{2}}.$

$a+b+c\ge 3\sqrt[3]{abc}.$

Suy ra $(1+a)(1+b)(1+c)$ $\ge 1+3{{\left( \sqrt[3]{abc} \right)}^{2}}+3\sqrt[3]{abc}+abc$ $={{\left( 1+\sqrt[3]{abc} \right)}^{3}}.$

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$

d) Áp dụng bất đẳng thức Cô-si cho hai số dương, ta có:

${{a}^{2}}\sqrt{bc}\le {{a}^{2}}\left( \frac{b+c}{2} \right).$

${{b}^{2}}\sqrt{ac}\le {{b}^{2}}\left( \frac{a+c}{2} \right).$

${{c}^{2}}\sqrt{ab}\le {{c}^{2}}\left( \frac{a+b}{2} \right).$

Suy ra ${{a}^{2}}\sqrt{bc}+{{b}^{2}}\sqrt{ac}+{{c}^{2}}\sqrt{ab}$ $\le \frac{{{a}^{2}}b+{{b}^{2}}a+{{a}^{2}}c+{{c}^{2}}a+{{b}^{2}}c+{{c}^{2}}b}{2}$ $(1).$

Mặt khác theo bất đẳng thức Cô-si cho ba số dương, ta có:

${{a}^{2}}b\le \frac{{{a}^{3}}+{{a}^{3}}+{{b}^{3}}}{3}.$

${{b}^{2}}a\le \frac{{{b}^{3}}+{{b}^{3}}+{{a}^{3}}}{3}.$

${{a}^{2}}c\le \frac{{{a}^{3}}+{{a}^{3}}+{{c}^{3}}}{3}.$

${{c}^{2}}a\le \frac{{{c}^{3}}+{{c}^{3}}+{{a}^{3}}}{3}.$

${{b}^{2}}c\le \frac{{{b}^{3}}+{{b}^{3}}+{{c}^{3}}}{3}.$

${{c}^{2}}b\le \frac{{{c}^{3}}+{{c}^{3}}+{{b}^{3}}}{3}.$

Suy ra ${{a}^{2}}b+{{b}^{2}}a+{{a}^{2}}c+{{c}^{2}}a+{{b}^{2}}c+{{c}^{2}}b$ $\le 2\left( {{a}^{3}}+{{b}^{3}}+{{c}^{3}} \right)$ $(2).$

Từ $(1)$ và $(2)$ suy ra ${{a}^{2}}\sqrt{bc}+{{b}^{2}}\sqrt{ac}+{{c}^{2}}\sqrt{ab}$ $\le {{a}^{3}}+{{b}^{3}}+{{c}^{3}}.$

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 3. Cho $a$, $b$, $c$, $d$ là các số dương. Chứng minh rằng:

a) $\frac{a+b+c+d}{4}\ge \sqrt[4]{abcd}.$

b) $\left( \frac{a}{{{b}^{3}}}+\frac{b}{{{c}^{3}}}+\frac{c}{{{d}^{3}}}+\frac{d}{{{a}^{3}}} \right)\left( a+b \right)\left( b+c \right)\ge 16.$

c) $\frac{a+b+c}{\sqrt[3]{abc}}+\frac{8abc}{(a+b)(b+c)(c+a)}\ge 4.$

a) Áp dụng bất đẳng thức Cô-si ta có:

$a+b\ge 2\sqrt{ab}.$

$c+d\ge 2\sqrt{c\text{d}}.$

$\sqrt{ab}+\sqrt{cd}$ $\ge 2\sqrt{\sqrt{ab}.\sqrt{cd}}$ $=2\sqrt[4]{abc\text{d}}.$

Suy ra $\frac{a+b+c+d}{4}$ $\ge \frac{2\sqrt{ab}+2\sqrt{cd}}{4}$ $\ge \sqrt[4]{abcd}.$

Dấu bằng xảy ra khi và chỉ khi $a=b=c=d.$

b) Áp dụng câu a, ta có:

$\frac{a}{{{b}^{3}}}+\frac{b}{{{c}^{3}}}+\frac{c}{{{d}^{3}}}+\frac{d}{{{a}^{3}}}$ $\ge 4\sqrt[4]{\frac{a}{{{b}^{3}}}.\frac{b}{{{c}^{3}}}.\frac{c}{{{d}^{3}}}.\frac{d}{{{a}^{3}}}}$ $=\frac{4}{\sqrt{abcd}}.$

Suy ra $\left( \frac{a}{{{b}^{3}}}+\frac{b}{{{c}^{3}}}+\frac{c}{{{d}^{3}}}+\frac{d}{{{a}^{3}}} \right)\left( a+b \right)\left( c+d \right)$ $\ge \frac{4}{\sqrt{abcd}}.2\sqrt{ab}.2\sqrt{cd}=16.$

Đẳng thức xảy ra khi và chỉ khi $a=b=c=d.$

c) Áp dụng câu a, ta có:

$VT=3.\frac{a+b+c}{3\sqrt[3]{abc}}+\frac{8abc}{(a+b)(b+c)(c+a)}$ $\ge 4\sqrt[4]{{{\left( \frac{a+b+c}{3\sqrt[3]{abc}} \right)}^{3}}\frac{8abc}{(a+b)(b+c)(c+a)}}$ $=4\sqrt[4]{\frac{8{{\left( a+b+c \right)}^{3}}}{27(a+b)(b+c)(c+a)}}.$

Như vậy ta chỉ cần chứng minh $4\sqrt[4]{\frac{8{{\left( a+b+c \right)}^{3}}}{27(a+b)(b+c)(c+a)}}\ge 4$ $\Leftrightarrow 8{{\left( a+b+c \right)}^{3}}$ $\ge 27\left( a+b \right)\left( b+c \right)\left( c+a \right)$ $(*).$

Áp dụng bất đẳng thức Cô-si cho ba số, ta có:

$\left( a+b \right)\left( b+c \right)\left( c+a \right)$ $\le {{\left( \frac{\left( a+b \right)+\left( b+c \right)+\left( c+a \right)}{3} \right)}^{3}}$ $=\frac{8{{\left( a+b+c \right)}^{3}}}{27}.$

Suy ra bất đẳng thức $(*)$ đúng nên bất đẳng thức ban đầu đúng.

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$

Nhận xét: Bất đẳng thức ở câu a là bất đẳng thức Cô-si cho bốn số không âm. Ta có bất đẳng thức Cô-si cho $n$ số không âm như sau:

Cho $n$ số không âm ${{a}_{i}}$ ($i=1, 2,.., n$). Khi đó ta có $\frac{{{a}_{1}}+{{a}_{2}}+…+{{a}_{n}}}{n}$ $\ge \sqrt[n]{{{a}_{1}}{{a}_{2}}…{{a}_{n}}}.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 4. Cho $a,b,c$ là số dương thỏa mãn ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}=3$. Chứng minh rằng:

a) ${{a}^{2}}b+{{b}^{2}}c+{{c}^{2}}a\le 3.$

b) $\frac{ab}{3+{{c}^{2}}}+\frac{bc}{3+{{a}^{2}}}+\frac{ca}{3+{{b}^{2}}}\le \frac{3}{4}.$

a) Ta có ${{\left( {{a}^{2}}+{{b}^{2}}+{{c}^{2}} \right)}^{2}}=9$ $\Leftrightarrow {{a}^{4}}+{{b}^{4}}+{{c}^{4}}+2{{a}^{2}}{{b}^{2}}+2{{b}^{2}}{{c}^{2}}+2{{c}^{2}}{{b}^{2}}=9$ $(1).$

Áp dụng bất đẳng thức Cô-si, ta có:

${{a}^{4}}+{{b}^{4}}\ge 2{{a}^{2}}{{b}^{2}}.$

${{b}^{4}}+{{c}^{4}}\ge 2{{b}^{2}}{{c}^{2}}.$

${{c}^{4}}+{{a}^{4}}\ge 2{{c}^{2}}{{a}^{2}}.$

Cộng vế với vế lại ta được: ${{a}^{4}}+{{b}^{4}}+{{c}^{4}}$ $\ge {{a}^{2}}{{b}^{2}}+{{b}^{2}}{{c}^{2}}+{{c}^{2}}{{a}^{2}}$ $(2).$

Từ $(1)$ và $(2)$ ta có: ${{a}^{2}}{{b}^{2}}+{{b}^{2}}{{c}^{2}}+{{c}^{2}}{{a}^{2}}\le 3$ $(3).$

Áp dụng bất đẳng thức Cô-si, ta có:

${{a}^{2}}+{{a}^{2}}{{b}^{2}}$ $\ge 2\sqrt{{{a}^{2}}.{{a}^{2}}{{b}^{2}}}=2{{a}^{2}}b.$

${{b}^{2}}+{{b}^{2}}{{c}^{2}}\ge 2{{b}^{2}}c.$

${{c}^{2}}+{{c}^{2}}{{a}^{2}}\ge 2{{c}^{2}}a.$

Cộng vế với vế ta được ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}+{{a}^{2}}{{b}^{2}}+{{b}^{2}}{{c}^{2}}+{{c}^{2}}{{a}^{2}}$ $\ge 2\left( {{a}^{2}}b+{{b}^{2}}c+{{c}^{2}}a \right)$ $(4).$

Từ giả thiết và $(3)$, $(4)$ suy ra ${{a}^{2}}b+{{b}^{2}}c+{{c}^{2}}a\le 3.$

Đẳng thức xảy ra khi và chỉ khi $a=b=c=1.$

b) Áp dụng bất đẳng thức Cô-si, ta có:

$3+{{a}^{2}}$ $=3+\left( 3-{{b}^{2}}-{{c}^{2}} \right)$ $=\left( 3-{{b}^{2}} \right)+\left( 3-{{c}^{2}} \right)$ $\ge 2\sqrt{\left( 3-{{b}^{2}} \right)\left( 3-{{c}^{2}} \right)}.$

Suy ra: $\frac{bc}{3+{{a}^{2}}}$ $\le \frac{bc}{2\sqrt{\left( 3-{{b}^{2}} \right)\left( 3-{{c}^{2}} \right)}}$ $=\frac{1}{2}\sqrt{\frac{{{b}^{2}}}{3-{{c}^{2}}}.\frac{{{c}^{2}}}{3-{{b}^{2}}}}$ $\le \frac{1}{4}\left( \frac{{{b}^{2}}}{3-{{c}^{2}}}+\frac{{{c}^{2}}}{3-{{b}^{2}}} \right)$ $=\frac{1}{4}\left( \frac{{{b}^{2}}}{{{b}^{2}}+{{a}^{2}}}+\frac{{{c}^{2}}}{{{c}^{2}}+{{a}^{2}}} \right).$

Tương tự ta có:

$\frac{ab}{3+{{c}^{2}}}$ $\le \frac{1}{4}\left( \frac{{{a}^{2}}}{{{a}^{2}}+{{c}^{2}}}+\frac{{{b}^{2}}}{{{b}^{2}}+{{c}^{2}}} \right).$

$\frac{ca}{3+{{b}^{2}}}$ $\le \frac{1}{4}\left( \frac{{{c}^{2}}}{{{c}^{2}}+{{b}^{2}}}+\frac{{{a}^{2}}}{{{a}^{2}}+{{b}^{2}}} \right).$

Cộng vế với vế ta được $\frac{ab}{3+{{c}^{2}}}+\frac{bc}{3+{{a}^{2}}}+\frac{ca}{3+{{b}^{2}}}$ $\le \frac{3}{4}.$

Đẳng thức xảy ra khi và chỉ khi $a=b=c=1.$

<!-- chunk:6 level:2 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Dạng toán 2. Kĩ thuật tách – thêm bớt – ghép cặp.
Phương pháp giải toán:

+ Để chứng minh bất đẳng thức ta thường phải biến đổi (nhân chia, thêm, bớt một biểu thức) để tạo biểu thức có thể giản ước được sau khi áp dụng bất đẳng thức Cô-si.

+ Khi gặp bất đẳng thức có dạng $x+y+z$ $\ge a+b+c$ (hoặc $xyz$ $\ge abc$), ta thường đi chứng minh $x+y$ $\ge 2a$ (hoặc $ab$ $\le {{x}^{2}}$), xây dựng các bất đẳng thức tương tự rồi cộng (hoặc nhân) vế với vế ta suy ra điều phải chứng minh.

+ Khi tách và áp dụng bất đẳng thức Cô-si ta dựa vào việc đảm bảo dấu bằng xảy ra (thường dấu bằng xảy ra khi các biến bằng nhau hoặc tại biên).

<!-- chunk:7 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 5. Cho $a$, $b$, $c$ là số dương. Chứng minh rằng:

a) $\frac{ab}{c}+\frac{bc}{a}+\frac{ac}{b}\ge a+b+c.$

b) $\frac{a}{{{b}^{2}}}+\frac{b}{{{c}^{2}}}+\frac{c}{{{a}^{2}}}$ $\ge \frac{1}{a}+\frac{1}{b}+\frac{1}{c}.$

a) Áp dụng bất đẳng thức Cô-si, ta có: $\frac{ab}{c}+\frac{bc}{a}$ $\ge 2\sqrt{\frac{ab}{c}.\frac{bc}{a}}=2b.$

Tương tự ta có: $\frac{bc}{a}+\frac{ac}{b}\ge 2c$, $\frac{ac}{b}+\frac{ba}{c}\ge 2a.$

Cộng vế với vế các bất đẳng thức trên ta được:

$2\left( \frac{ab}{c}+\frac{bc}{a}+\frac{ac}{b} \right)$ $\ge 2\left( a+b+c \right)$ $\Leftrightarrow \frac{ab}{c}+\frac{bc}{a}+\frac{ac}{b}$ $\ge a+b+c.$

Đẳng thức xảy ra khi $a=b=c.$

b) Áp dụng bất đẳng thức Cô-si, ta có: $\frac{a}{{{b}^{2}}}+\frac{1}{a}$ $\ge 2\sqrt{\frac{a}{{{b}^{2}}}.\frac{1}{a}}=\frac{2}{b}.$

Tương tự ta có: $\frac{b}{{{c}^{2}}}+\frac{1}{b}\ge \frac{2}{c}$, $\frac{c}{{{a}^{2}}}+\frac{1}{c}\ge \frac{2}{a}.$

Cộng vế với vế các bất đẳng thức trên ta được:

$\frac{a}{{{b}^{2}}}+\frac{b}{{{c}^{2}}}+\frac{c}{{{a}^{2}}}+\frac{1}{a}+\frac{1}{b}+\frac{1}{c}$ $\ge \frac{2}{a}+\frac{2}{b}+\frac{2}{c}$ $\Leftrightarrow \frac{a}{{{b}^{2}}}+\frac{b}{{{c}^{2}}}+\frac{c}{{{a}^{2}}}$ $\ge \frac{1}{a}+\frac{1}{b}+\frac{1}{c}.$

Đẳng thức xảy ra khi $a=b=c.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 6. Cho $a,b,c$ dương sao cho ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}=3$. Chứng minh rằng:

a) $\frac{{{a}^{3}}{{b}^{3}}}{c}+\frac{{{b}^{3}}{{c}^{3}}}{a}+\frac{{{c}^{3}}{{a}^{3}}}{b}\ge 3abc.$

b) $\frac{ab}{c}+\frac{bc}{a}+\frac{ca}{b}\ge 3.$

a) Áp dụng bất đẳng thức Cô-si, ta có: $\frac{{{a}^{3}}{{b}^{3}}}{c}+\frac{{{b}^{3}}{{c}^{3}}}{a}$ $\ge 2\sqrt{\frac{{{a}^{3}}{{b}^{3}}}{c}.\frac{{{b}^{3}}{{c}^{3}}}{a}}=2{{b}^{3}}ac.$

Tương tự ta có: $\frac{{{b}^{3}}{{c}^{3}}}{a}+\frac{{{c}^{3}}{{a}^{3}}}{b}\ge 2ab{{c}^{3}}$, $\frac{{{c}^{3}}{{a}^{3}}}{b}+\frac{{{a}^{3}}{{b}^{3}}}{c}\ge 2{{a}^{3}}bc.$

Cộng vế với vế ta có $2\left( \frac{{{a}^{3}}{{b}^{3}}}{c}+\frac{{{b}^{3}}{{c}^{3}}}{a}+\frac{{{c}^{3}}{{a}^{3}}}{b} \right)$ $\ge 2abc\left( {{a}^{2}}+{{b}^{2}}+{{c}^{2}} \right)$ $\Leftrightarrow \frac{{{a}^{3}}{{b}^{3}}}{c}+\frac{{{b}^{3}}{{c}^{3}}}{a}+\frac{{{c}^{3}}{{a}^{3}}}{b}\ge 3abc.$

Đẳng thức xảy ra khi $a=b=c=1.$

b) Bất đẳng thức tương đương với: ${{\left( \frac{ab}{c}+\frac{bc}{a}+\frac{ca}{b} \right)}^{2}}\ge 9$ $\Leftrightarrow {{\left( \frac{ab}{c} \right)}^{2}}+{{\left( \frac{bc}{a} \right)}^{2}}+{{\left( \frac{ca}{b} \right)}^{2}}$ $+2\left( {{a}^{2}}+{{b}^{2}}+{{c}^{2}} \right)\ge 9$ $\Leftrightarrow {{\left( \frac{ab}{c} \right)}^{2}}+{{\left( \frac{bc}{a} \right)}^{2}}+{{\left( \frac{ca}{b} \right)}^{2}}\ge 3.$

Áp dụng bất đẳng thức Cô-si, ta có: ${{\left( \frac{ab}{c} \right)}^{2}}+{{\left( \frac{bc}{a} \right)}^{2}}$ $\ge 2\sqrt{{{\left( \frac{ab}{c} \right)}^{2}}.{{\left( \frac{bc}{a} \right)}^{2}}}=2{{b}^{2}}.$

Tương tự ta có: ${{\left( \frac{bc}{a} \right)}^{2}}+{{\left( \frac{ca}{b} \right)}^{2}}\ge 2{{c}^{2}}$, ${{\left( \frac{ca}{b} \right)}^{2}}+{{\left( \frac{ab}{c} \right)}^{2}}\ge 2{{\text{a}}^{2}}.$

Cộng vế với vế và rút gọn ta được: ${{\left( \frac{ab}{c} \right)}^{2}}+{{\left( \frac{bc}{a} \right)}^{2}}+{{\left( \frac{ca}{b} \right)}^{2}}\ge 3.$

Đẳng thức xảy ra khi $a=b=c=1.$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 7. Cho $a,b,c$ là số dương thỏa mãn $a+b+c=3$. Chứng minh rằng:

a) $8\left( a+b \right)\left( b+c \right)\left( c+a \right)$ $\le \left( 3+a \right)\left( 3+b \right)\left( 3+c \right).$

b) $\left( 3-2a \right)\left( 3-2b \right)\left( 3-2c \right)\le abc.$

a) Áp dụng bất đẳng thức Cô-si, ta có: $\left( a+b \right)\left( b+c \right)$ $\le {{\left( \frac{\left( a+b \right)+\left( b+c \right)}{2} \right)}^{2}}$ $=\frac{{{\left( 3+a \right)}^{2}}}{4}.$

Tương tự ta có: $\left( b+c \right)\left( c+a \right)$ $\le \frac{{{\left( 3+c \right)}^{2}}}{4}$, $\left( c+a \right)\left( a+b \right)$ $\le \frac{{{\left( 3+a \right)}^{2}}}{4}.$

Nhân vế với vế lại ta được: ${{\left[ \left( a+b \right)\left( b+c \right)\left( c+a \right) \right]}^{2}}$ $\le 64{{\left[ \left( 3+a \right)\left( 3+b \right)\left( 3+c \right) \right]}^{2}}.$

Suy ra $8\left( a+b \right)\left( b+c \right)\left( c+a \right)$ $\le \left( 3+a \right)\left( 3+b \right)\left( 3+c \right).$

Đẳng thức xảy ra khi $a=b=c=1.$

b)

Trường hợp 1: Với $\left( 3-2a \right)\left( 3-2b \right)\left( 3-2c \right)\le 0$: bất đẳng thức hiển nhiên đúng.

Trường hợp 2: Với $\left( 3-2a \right)\left( 3-2b \right)\left( 3-2c \right)>0$:

+ Nếu cả ba số $\left( 3-2a \right)$, $\left( 3-2b \right)$, $\left( 3-2c \right)$ đều dương. Áp dụng bất đẳng thức Cô-si, ta có: $\left( 3-2a \right)\left( 3-2b \right)$ $\le {{\left( \frac{\left( 3-2a \right)+\left( 3-2b \right)}{2} \right)}^{2}}={{c}^{2}}.$

Tương tự, ta có: $\left( 3-2b \right)\left( 3-2c \right)\le {{a}^{2}}$, $\left( 3-2c \right)\left( 3-2a \right)\le {{b}^{2}}.$

Nhân vế với vế ta được ${{\left[ \left( 3-2a \right)\left( 3-2b \right)\left( 3-2c \right) \right]}^{2}}$ $\le {{a}^{2}}{{b}^{2}}{{c}^{2}}.$

Hay $\left( 3-2a \right)\left( 3-2b \right)\left( 3-2c \right)\le abc.$

+ Nếu hai trong ba số $\left( 3-2a \right)$, $\left( 3-2b \right)$, $\left( 3-2c \right)$ âm và một số dương. Không mất tính tổng quát giả sử $3-2a<0$, $3-2b<0$ suy ra $6-2a-2b<0$ $\Leftrightarrow c<0$ (không xảy ra).

Vậy bất đẳng thức được chứng minh.

Đẳng thức xảy ra $\Leftrightarrow a=b=c=1.$

[ads]

<!-- chunk:10 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 8. Cho $a,b,c$ là các số dương. Chứng minh rằng $\frac{{{a}^{2}}}{b+c}+\frac{{{b}^{2}}}{c+a}+\frac{{{c}^{2}}}{a+b}$ $\ge \frac{a+b+c}{2}.$

Áp dụng bất đẳng thức Cô-si cho hai số thực dương, ta có: $\frac{{{a}^{2}}}{b+c}+\frac{b+c}{4}$ $\ge 2\sqrt{\frac{{{a}^{2}}}{b+c}.\frac{b+c}{4}}=a.$

Tương tự ta có: $\frac{{{b}^{2}}}{c+a}+\frac{c+a}{4}\ge b$, $\frac{{{c}^{2}}}{a+b}+\frac{a+b}{4}\ge c.$

Cộng ba bất đẳng thức này lại với nhau ta đươc: $\frac{{{a}^{2}}}{b+c}+\frac{{{b}^{2}}}{c+a}+\frac{{{c}^{2}}}{a+b}+\frac{a+b+c}{2}$ $\ge a+b+c$ $\Leftrightarrow \frac{{{a}^{2}}}{b+c}+\frac{{{b}^{2}}}{c+a}+\frac{{{c}^{2}}}{a+b}$ $\ge \frac{a+b+c}{2}.$

Đẳng thức xảy ra $\Leftrightarrow a=b=c.$

Lưu ý: Việc ta ghép $\frac{{{a}^{2}}}{b+c}+\frac{b+c}{4}$ và đánh giá như trên là vì những lí do sau:

+ Thứ nhất là ta cần làm mất mẫu số ở các đại lượng vế trái (vì vế phải không có phân số), chẳng hạn đại lượng $\frac{{{a}^{2}}}{b+c}$ khi đó ta sẽ áp dụng bất đẳng thức Cô-si cho đại lượng đó với một đại lượng chứa $b+c.$

+ Thứ hai là ta cần lưu ý tới điều kiện xảy ra đẳng thức ở bất đẳng thức Cô-si là khi hai số đó bằng nhau. Ta dự đoán dấu bằng xảy ra khi $a=b=c$ khi đó $\frac{{{a}^{2}}}{b+c}=\frac{a}{2}$ và $b+c=2a$ do đó ta ghép như trên.

<!-- chunk:11 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 9. Cho $a,b,c$ là số dương thỏa mãn $abc=1$. Chứng minh rằng $\frac{1}{{{a}^{2}}}+\frac{1}{{{b}^{2}}}+\frac{1}{{{c}^{2}}}+3$ $\ge 2\left( a+b+c \right).$

Ta có $\left[ \left( a-1 \right)\left( b-1 \right) \right]\left[ \left( b-1 \right)\left( c-1 \right) \right]\left[ \left( c-1 \right)\left( a-1 \right) \right]$ $={{\left( a-1 \right)}^{2}}{{\left( b-1 \right)}^{2}}{{\left( c-1 \right)}^{2}}\ge 0.$

Do đó không mất tính tổng quát giả sử $\left( a-1 \right)\left( b-1 \right)\ge 0$ $\Leftrightarrow ab+1\ge a+b$ $\Leftrightarrow 2\left( ab+c+1 \right)$ $\ge 2\left( a+b+c \right).$

Do đó ta chỉ cần chứng minh $\frac{1}{{{a}^{2}}}+\frac{1}{{{b}^{2}}}+\frac{1}{{{c}^{2}}}+3$ $\ge 2\left( ab+c+1 \right)$ $\Leftrightarrow \frac{1}{{{a}^{2}}}+\frac{1}{{{b}^{2}}}+\frac{1}{{{c}^{2}}}+1$ $\ge 2\left( ab+c \right).$

Áp dụng bất đẳng thức Cô-si, ta có $\frac{1}{{{a}^{2}}}+\frac{1}{{{b}^{2}}}\ge \frac{2}{ab}=2c$, $\frac{1}{{{c}^{2}}}+1\ge \frac{2}{c}=2ab$ (do $abc=1$).

Cộng vế với vế ta được $\frac{1}{{{a}^{2}}}+\frac{1}{{{b}^{2}}}+\frac{1}{{{c}^{2}}}+1$ $\ge 2\left( ab+c \right).$

Đẳng thức xảy ra $\Leftrightarrow a=b=c=1.$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 10. Tìm giá trị nhỏ nhất của biểu thức:

a) $f(x)=\frac{{{\left( x-1 \right)}^{2}}}{x-2}$ với $x>2.$

b) $g(x)=2x+\frac{1}{{{\left( x+1 \right)}^{2}}}$ với $x>-1.$

c) $h\left( x \right)=x+\frac{3}{x}$ với $x\ge 2.$

d) $k\left( x \right)=2x+\frac{1}{{{x}^{2}}}$ với $0<x\le \frac{1}{2}.$

a) Ta có $f(x)$ $=\frac{{{x}^{2}}-2x+1}{x-2}$ $=x-2+\frac{1}{x-2}+2.$

Do $x>2$ nên $x-2>0$, $\frac{1}{x-2}>0$.

Áp dụng bất đẳng thức Cô-si, ta có: $x-2+\frac{1}{x-2}$ $\ge 2\sqrt{\left( x-2 \right).\frac{1}{x-2}}=2.$

Suy ra $f\left( x \right)\ge 4.$

Đẳng thức xảy ra $\Leftrightarrow x-2=\frac{1}{x-2}$ $\Leftrightarrow {{\left( x-2 \right)}^{2}}=1$ $\Leftrightarrow x=1$ (loại) hoặc $x=3$ (thỏa mãn).

Vậy $\min f\left( x \right)=4$ khi và chỉ khi $x=3.$

b) Do $x>-1$ nên $x+1>0$.

Áp dụng bất đẳng thức Cô-si, ta có:

$g(x)$ $=\left( x+1 \right)+\left( x+1 \right)+\frac{1}{{{\left( x+1 \right)}^{2}}}-2$ $\ge 3\sqrt[3]{\left( x+1 \right).\left( x+1 \right).\frac{1}{{{\left( x+1 \right)}^{2}}}}-2=1.$

Đẳng thức xảy ra $\Leftrightarrow x+1=\frac{1}{{{\left( x+1 \right)}^{2}}}$ $\Leftrightarrow {{\left( x+1 \right)}^{3}}=1$ $\Leftrightarrow x=0$ (thỏa mãn).

Vậy $\min g\left( x \right)=1$ khi và chỉ khi $x=0.$

c) Ta có $h\left( x \right)=\left( \frac{3}{x}+\frac{3x}{4} \right)+\frac{x}{4}.$

Áp dụng bất đẳng thức Cô-si, ta có $\frac{3}{x}+\frac{3x}{4}$ $\ge 2\sqrt{\frac{3}{x}.\frac{3x}{4}}=3.$

Mặt khác $x\ge 2$ suy ra $h\left( x \right)=\left( \frac{3}{x}+\frac{3x}{4} \right)+\frac{x}{4}$ $\ge 3+\frac{2}{4}=\frac{7}{2}.$

Đẳng thức xảy ra
\Leftrightarrow \left\{ \begin{matrix}
\frac{3}{x}=\frac{3x}{4} \\
x=2 \\
\end{matrix} \right.
$\Leftrightarrow x=2.$

Vậy $\min h\left( x \right)=\frac{7}{2}$ khi và chỉ khi $x=2.$

d) Ta có $k\left( x \right)=x+x+\frac{1}{8{{x}^{2}}}+\frac{7}{8{{x}^{2}}}.$

Áp dụng bất đẳng thức Cô-si, ta có: $x+x+\frac{1}{8{{x}^{2}}}$ $\ge 3\sqrt[3]{x.x.\frac{1}{8{{x}^{2}}}}=\frac{3}{2}.$

Mặt khác $0<x\le \frac{1}{2}$ $\Rightarrow \frac{7}{8{{x}^{2}}}$ $\ge \frac{7}{2}$ suy ra $k\left( x \right)$ $\ge \frac{3}{2}+\frac{7}{2}=5.$

Đẳng thức xảy ra
\Leftrightarrow \left\{ \begin{matrix}
x=\frac{1}{8{{x}^{2}}} \\
x=\frac{1}{2} \\
\end{matrix} \right.
$\Leftrightarrow x=\frac{1}{2}.$

Vậy $\min k\left( x \right)=5$ khi và chỉ khi $x=\frac{1}{2}.$

**Dạng toán 3. Kĩ thuật tham số hóa.

****Phương pháp giải toán**: Nhiều khi không dự đoán được dấu bằng xảy ra (để tách ghép cho hợp lí) chúng ta cần đưa tham số vào rồi chọn sau sao cho dấu bằng xảy ra.

<!-- chunk:13 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 11. Cho $a,b,c$ là số dương thỏa mãn ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}=1$. Tìm giá trị lớn nhất của $A=\left( 1+2a \right)\left( 1+2bc \right).$

Phân tích:

Rõ ràng ta sẽ đánh giá biểu thức $A$ để làm xuất hiện ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}.$

Trước tiên ta sẽ đánh giá $a$ qua ${{a}^{2}}$ bởi ${{a}^{2}}+{{m}^{2}}\ge 2ma$ $\Rightarrow 2a\le \frac{{{a}^{2}}}{m}+m$ (với $m>0$).

Do $b,c$ bình đẳng nên dự đoán dấu bằng $A$ đạt giá trị nhỏ nhất khi $b=c$ nên ta đánh giá $2bc\le {{b}^{2}}+{{c}^{2}}.$

Suy ra $A\le \left( \frac{{{a}^{2}}}{m}+m+1 \right)\left( 1+{{b}^{2}}+{{c}^{2}} \right)=B$.

Tiếp tục ta sẽ sử dụng bất đẳng thức Cô-si dưới dạng $xy\le {{\left( \frac{x+y}{2} \right)}^{2}}$ để làm xuất hiện ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}$ nên ta sẽ tách như sau:

$B=\frac{1}{m}\left( {{a}^{2}}+{{m}^{2}}+m \right)\left( 1+{{b}^{2}}+{{c}^{2}} \right)$ $\le \frac{1}{m}{{\left( \frac{\left( {{a}^{2}}+{{m}^{2}}+m \right)+\left( 1+{{b}^{2}}+{{c}^{2}} \right)}{2} \right)}^{2}}.$

Suy ra $\text{A}\le \frac{1}{4m}{{\left( {{m}^{2}}+m+2 \right)}^{2}}.$

Dấu bằng xảy ra khi $a=m$, $b=c$, ${{a}^{2}}+{{m}^{2}}+m=1+{{b}^{2}}+{{c}^{2}}$ và ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}=1.$

Từ đây ta có $m=\frac{2}{3}.$

Lời giải:

Áp dụng bất đẳng thức Cô-si, ta có ${{a}^{2}}+\frac{4}{9}\ge \frac{4}{3}a$ $\Rightarrow 2a\le \frac{3{{a}^{2}}}{2}+\frac{2}{3}$ và $2bc\le {{b}^{2}}+{{c}^{2}}.$

Suy ra $A\le \left( \frac{3{{a}^{2}}}{2}+\frac{2}{3}+1 \right)\left( {{b}^{2}}+{{c}^{2}}+1 \right).$

Áp dụng bất đẳng thức Cô-si, ta có:

$\left( \frac{3{{a}^{2}}}{2}+\frac{2}{3}+1 \right)\left( {{b}^{2}}+{{c}^{2}}+1 \right)$ $=\frac{3}{2}\left( {{a}^{2}}+\frac{10}{9} \right)\left( {{b}^{2}}+{{c}^{2}}+1 \right)$ $\le \frac{3}{2}{{\left( \frac{{{a}^{2}}+\frac{10}{9}+{{b}^{2}}+{{c}^{2}}+1}{2} \right)}^{2}}=\frac{98}{27}.$

Suy ra $\text{A}\le \frac{98}{27}.$

Đẳng thức xảy ra khi và chỉ khi
\left\{ \begin{align}
& a=\frac{2}{3} \\
& b=c \\
& {{a}^{2}}+\frac{10}{9}={{b}^{2}}+{{c}^{2}}+1 \\
& {{a}^{2}}+{{b}^{2}}+{{c}^{2}}=1 \\
\end{align} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{align}
& a=\frac{2}{3} \\
& b=c=\sqrt{\frac{5}{18}} \\
\end{align} \right.
$$

Vậy $\max A=\frac{98}{27}$ khi và chỉ khi $a=\frac{2}{3}$ và $b=c=\sqrt{\frac{5}{18}}.$

<!-- chunk:14 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 12. Cho $a,b,c$ là số dương thỏa mãn $2a+4b+3{{c}^{2}}=68$. Tìm giá trị nhỏ nhất của $A={{a}^{2}}+{{b}^{2}}+{{c}^{3}}.$

Phân tích:

Ta cần đánh giá biểu thức $A$ qua biểu thức $2a+4b+3{{c}^{2}}$, do đó ta sẽ cho thêm vào các tham số vào và đánh giá như sau ($m,n,p$ dương).

${{a}^{2}}+{{m}^{2}}\ge 2am$, ${{b}^{2}}+{{n}^{2}}\ge 2bn$ và $\frac{{{c}^{3}}}{2}+\frac{{{c}^{3}}}{2}+4{{p}^{3}}\ge 3p{{c}^{2}}.$

Suy ra ${{a}^{2}}+{{b}^{2}}+{{c}^{3}}+{{m}^{2}}+{{n}^{2}}+4{{p}^{3}}$ $\ge 2am+2bn+3pc$ $(*).$

Để $2am+2bn+3p{{c}^{2}}$ có thể bội số của $2a+4b+3{{c}^{2}}$ thì $\frac{2m}{2}=\frac{2n}{4}=\frac{3p}{3}$ $\Leftrightarrow m=\frac{n}{2}=p.$

Mặt khác dấu bằng ở bất đẳng thức $(*)$ xảy ra khi $a=m$, $b=n$, $c=2p.$

Hay $a=m$, $b=2m$, $c=2m$ $\Rightarrow 2m+4.\left( 2m \right)+3{{\left( 2m \right)}^{2}}=68$ $\Leftrightarrow 12{{m}^{2}}+10m-68=0$ $\Leftrightarrow m=2$ (nhận) hoặc $m=-\frac{17}{6}$ (loại).

Suy ra $p=2$, $n=4.$

Lời giải:

Áp dụng bất đẳng thức Cô-si, ta có:

${{a}^{2}}+4\ge 4a$, ${{b}^{2}}+16\ge 8b$ và $\frac{{{c}^{3}}}{2}+\frac{{{c}^{3}}}{2}+32\ge 6{{c}^{2}}.$

Cộng vế với vế ta được: ${{a}^{2}}+{{b}^{2}}+{{c}^{3}}+52$ $\ge 4a+8b+6{{c}^{2}}$, kết hợp với $2a+4b+3{{c}^{2}}=68.$

Suy ra ${{a}^{2}}+{{b}^{2}}+{{c}^{3}}\ge 84.$

Đẳng thức xảy ra khi và chỉ khi $a=2$, $b=4$, $c=4.$

Vậy $\min \text{A}=84$ $\Leftrightarrow a=2$, $b=4$, $c=4.$

<!-- chunk:15 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 13. Cho $a,b,c$ là các số thực dương. Tìm giá trị lớn nhất của biểu thức: $P=\frac{\sqrt{bc}}{a+2\sqrt{bc}}+\frac{\sqrt{ca}}{b+2\sqrt{ca}}+\frac{\sqrt{ab}}{c+2\sqrt{ab}}.$

Áp dụng bất đẳng thức Cô-si, ta có: $\frac{\sqrt{bc}}{a+2\sqrt{bc}}$ $=\frac{1}{2}\left( 1-\frac{a}{a+2\sqrt{bc}} \right)$ $\le \frac{1}{2}\left( 1-\frac{a}{a+b+c} \right).$

Tương tự ta có: $\frac{\sqrt{ca}}{b+2\sqrt{ca}}\le \frac{1}{2}\left( 1-\frac{b}{a+b+c} \right)$, $\frac{\sqrt{ab}}{c+2\sqrt{ab}}\le \frac{1}{2}\left( 1-\frac{c}{a+b+c} \right).$

Cộng vế với vế các bất đẳng thức trên ta được: $P\le \frac{1}{2}\left( 3-\frac{a}{a+b+c}-\frac{b}{a+b+c}-\frac{c}{a+b+c} \right)=1.$

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$

Vậy $\min P=1$ $\Leftrightarrow a=b=c.$

<!-- chunk:16 level:3 source:https://toanmath.com/2018/09/ki-thuat-su-dung-bat-dang-thuc-co-si-cauchy-de-giai-toan.html -->
## Ví dụ 14. Cho $a,b,c$ là các số thực không âm thỏa mãn $a+b+c=3$. Chứng minh rằng:

a) $\frac{a}{1+{{b}^{2}}}+\frac{b}{1+{{c}^{2}}}+\frac{c}{1+{{a}^{2}}}\ge \frac{3}{2}.$

b) $\frac{{{a}^{2}}}{a+2{{b}^{3}}}+\frac{{{b}^{2}}}{b+2{{c}^{3}}}+\frac{{{c}^{2}}}{c+2{{a}^{3}}}\ge 1.$

a) Áp dụng bất đẳng thức Cô-si, ta có: $\frac{a}{1+{{b}^{2}}}$ $=\frac{a\left( 1+{{b}^{2}}-{{b}^{2}} \right)}{1+{{b}^{2}}}$ $=a-\frac{a{{b}^{2}}}{1+{{b}^{2}}}$ $\ge a-\frac{a{{b}^{2}}}{2b}$ $=a-\frac{ab}{2}.$

Tương tự ta có: $\frac{b}{1+{{c}^{2}}}$ $\ge b-\frac{bc}{2}$ và $\frac{c}{1+{{a}^{2}}}$ $\ge c-\frac{ca}{2}.$

Cộng vế theo vế các bất đẳng thức trên ta được:

$\frac{a}{1+{{b}^{2}}}+\frac{b}{1+{{c}^{2}}}+\frac{c}{1+{{a}^{2}}}$ $\ge a+b+c-\frac{ab+bc+ca}{2}$ $=3-\frac{ab+bc+ca}{2}.$

Mặt khác ta có: ${{\left( a+b+c \right)}^{2}}$ $\ge 3\left( ab+bc+ca \right)$ $\Rightarrow ab+bc+ca\le 3.$

Do đó $\frac{a}{1+{{b}^{2}}}+\frac{b}{1+{{c}^{2}}}+\frac{c}{1+{{a}^{2}}}$ $\ge 3-\frac{3}{2}=\frac{3}{2}.$

Đẳng thức xảy ra khi và chỉ khi $a=b=c=1.$

b) Theo bất đẳng thức Cô-si, ta có:

$\frac{{{a}^{2}}}{a+2{{b}^{3}}}$ $=\frac{a\left( a+2{{b}^{3}} \right)-2a{{b}^{3}}}{a+2{{b}^{3}}}$ $\ge a-\frac{2a{{b}^{3}}}{3\sqrt[3]{a{{b}^{6}}}}$ $=a-\frac{2b\sqrt[3]{{{a}^{2}}}}{3}.$

Tương tự ta có: $\frac{{{b}^{2}}}{b+2{{c}^{3}}}$ $\ge b-\frac{2c\sqrt[3]{b}}{3}$, $\frac{{{c}^{2}}}{c+2{{a}^{3}}}$ $\ge c-\frac{2a\sqrt[3]{c}}{3}.$

Cộng vế theo vế các bất đẳng thức trên ta được:

$\frac{{{a}^{2}}}{a+2{{b}^{3}}}+\frac{{{b}^{2}}}{b+2{{c}^{3}}}+\frac{{{c}^{2}}}{c+2{{a}^{3}}}$ $\ge a+b+c-\frac{2}{3}\left( b\sqrt[3]{{{a}^{2}}}+a\sqrt[3]{{{c}^{2}}}+c\sqrt[3]{{{b}^{2}}} \right).$

Mặt khác $a+b+c=3$ do đó ta chỉ cần chứng minh: $b\sqrt[3]{{{a}^{2}}}+c\sqrt[3]{{{b}^{2}}}+a\sqrt[3]{{{c}^{2}}}\le 3.$

Thật vậy, theo bất đẳng thức Cô-si ta có: $b\sqrt[3]{{{a}^{2}}}\le \frac{1}{3}b.\left( a+a+1 \right)$ $=\frac{2ab+b}{3}.$

Tương tự ta có: $c\sqrt[3]{{{b}^{2}}}\le \frac{2bc+c}{3}$, $a\sqrt[3]{{{c}^{2}}}\le \frac{2ca+a}{3}.$

Cộng vế theo vế các bất đẳng thức trên ta có:

$b\sqrt[3]{{{a}^{2}}}+c\sqrt[3]{{{b}^{2}}}+a\sqrt[3]{{{c}^{2}}}$ $\le \frac{2ab+b}{3}+\frac{2bc+c}{3}+\frac{2ca+a}{3}$ $=\frac{2}{3}\left( ab+bc+ca \right)$ $+\frac{1}{3}\left( a+b+c \right).$

Từ đó suy ra: $b\sqrt[3]{{{a}^{2}}}+c\sqrt[3]{{{b}^{2}}}+a\sqrt[3]{{{c}^{2}}}$ $\le \frac{2}{3}.3+\frac{1}{3}.3=3.$

Đẳng thức xảy ra khi và chỉ khi $a=b=c=1.$