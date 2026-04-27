# Chứng minh bất đẳng thức bằng phương pháp biến đổi tương đương

<!-- chunk:0 level:0 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
Bài viết hướng dẫn cách chứng minh bất đẳng thức bằng phương pháp biến đổi tương đương thông qua các ví dụ minh họa cụ thể có lời giải chi tiết.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## A. KIẾN THỨC CẦN NẮM VỮNG

Giả sử ta cần chứng minh bất đẳng thức $A\ge B$, tư tưởng của phương pháp là biến đổi tương đương bất đẳng thức trên thành một bất đẳng thức đúng mà phổ biến là các dạng sau:

+ Sử dụng định nghĩa bất đẳng thức: $A\ge B$ $\Leftrightarrow A-B\ge 0.$

+ Dạng tổng bình phương: $A\ge B$ $\Leftrightarrow m{{X}^{2}}+n{{Y}^{2}}+k{{Z}^{2}}\ge 0$, với các số $m$, $n$, $k$ dương.

+ Dạng tích hai thừa số cùng dấu: $A\ge B$ $\Leftrightarrow X.Y\ge 0$ hoặc $A\ge B$ $\Leftrightarrow {{X}^{2n}}.Y\ge 0.$

+ Xây dựng các bất đẳng thức từ các điều kiện ban đầu: Nếu $x,y,z\in [a,b]$ thì ta nghĩ ngay tới một trong các bất đẳng thức đúng sau đây:

$\left( x-a \right)\left( x-b \right)\le 0.$

$\left( x-a \right)\left( y-a \right)\left( z-a \right)\ge 0.$

$\left( x-b \right)\left( y-b \right)\left( z-b \right)\le 0.$

Một số đẳng thức cần ghi nhớ:

• ${{\left( a\pm b \right)}^{2}}={{a}^{2}}\pm 2ab+{{b}^{2}}.$

• ${{a}^{2}}+{{b}^{2}}$ $=\frac{{{\left( a+b \right)}^{2}}}{2}+\frac{{{\left( a-b \right)}^{2}}}{2}.$

• ${{\left( a+b+c \right)}^{2}}$ $={{a}^{2}}+{{b}^{2}}+{{c}^{2}}$ $+2ab+2bc+2ca.$

• $\left( a+b \right)\left( b+c \right)\left( c+a \right)$ $={{a}^{2}}b+a{{b}^{2}}+{{b}^{2}}c+b{{c}^{2}}$ $+{{c}^{2}}a+c{{a}^{2}}+2abc.$

• $\left( a+b+c \right)\left( ab+bc+ca \right)$ $={{a}^{2}}b+a{{b}^{2}}+{{b}^{2}}c+b{{c}^{2}}$ $+{{c}^{2}}a+c{{a}^{2}}+3abc.$

• $\left( a+b \right)\left( b+c \right)\left( c+a \right)+abc$ $=\left( a+b+c \right)\left( ab+bc+ca \right).$

• $\left( a+1 \right)\left( b+1 \right)\left( c+1 \right)$ $=abc+ab+bc+ca$ $+a+b+c+1.$

• $\left( a-1 \right)\left( b-1 \right)\left( c-1 \right)$ $=abc-\left( ab+bc+ca \right)$ $+a+b+c-1.$

• ${{a}^{3}}+{{b}^{3}}+{{c}^{3}}-3abc$ $=\left( a+b+c \right)\left( {{a}^{2}}+{{b}^{2}}+{{c}^{2}}-ab-bc-ca \right).$

• ${{\left( a+b+c \right)}^{3}}$ $={{a}^{3}}+{{b}^{3}}+{{c}^{3}}$ $+3\left( a+b \right)\left( b+c \right)\left( c+a \right).$

• $\left( a+b+c \right)\left( {{a}^{2}}+{{b}^{2}}+{{c}^{2}} \right)$ $={{a}^{3}}+{{b}^{3}}+{{c}^{3}}$ $+{{a}^{2}}b+a{{b}^{2}}+{{b}^{2}}c+b{{c}^{2}}+{{c}^{2}}a+c{{a}^{2}}.$

Một số bất đẳng thức cơ bản:

• ${{a}^{2}}+{{b}^{2}}\ge 2ab.$

• $2\left( {{a}^{2}}+{{b}^{2}} \right)$ $\ge {{\left( a+b \right)}^{2}}$ $\ge 4ab.$

• ${{a}^{2}}+{{b}^{2}}-ab$ $\ge \frac{3{{\left( a+b \right)}^{2}}}{4}.$

• ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}$ $\ge ab+bc+ca.$

• $3\left( {{a}^{2}}+{{b}^{2}}+{{c}^{2}} \right)$ $\ge {{\left( a+b+c \right)}^{2}}$ $\ge 3\left( ab+bc+ca \right).$

• $3\left( {{a}^{4}}+{{b}^{4}}+{{c}^{4}} \right)$ $\ge {{\left( ab+bc+ca \right)}^{2}}$ $\ge 3abc\left( a+b+c \right).$

• Bất đẳng thức tam giác: Cho $a$, $b$, $c$ là độ dài ba cạnh của một tam giác, khi đó:
\left\{ \begin{align}
& \left| b-c \right|<a<b+c \\
& \left| c-a \right|<b<c+a \\
& \left| a-b \right|<c<a+b \\
\end{align} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{align}
& a+b-c>0 \\
& b+c-a>0 \\
& c+a-b>0 \\
\end{align} \right.
**Một số kỹ thuật cơ bản khi chứng minh bất đẳng thức bằng phương pháp biến đổi tương đương**:

+ Kỹ thuật xét hiệu hai biểu thức.

+ Kỹ thuật sử dụng các hằng đẳng thức.

+ Kỹ thuật thêm bớt một hằng số, một biểu thức.

+ Kỹ thuật đặt biến phụ.

+ Kỹ thuật sắp thứ tự các biến.

+ Kỹ thuật khai thác tính bị chặn của các biến.

<!-- chunk:2 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 1. Cho $a$, $b$, $c$ là các số thực bất kì. Chứng minh rẳng:

a) ${a^2} + {b^2} + {c^2}$ $\ge ab + bc + ca.$

b) ${a^2} + {b^2} + {c^2} + 3$ $\ge 2\left( {a + b + c} \right).$

Phân tích: Các bất đẳng thức trên khá quen thuộc, ta có thể giải bằng cách xét hiệu vế trái và vế phải rồi phân tích thành tổng các bình phương.

Lời giải:

a) Xét hiệu hai vế của bất đẳng thức:

$\left( {{a^2} + {b^2} + {c^2}} \right)$ $– \left( {ab + bc + ca} \right)$ $= \frac{{{a^2} – 2ab + {b^2} + {b^2} – 2bc + {c^2} + {c^2} – 2ca + {a^2}}}{2}$ $= \frac{{{{\left( {a – b} \right)}^2} + {{\left( {b – c} \right)}^2} + {{\left( {c – a} \right)}^2}}}{2} \ge 0.$

Suy ra: ${a^2} + {b^2} + {c^2}$ $\ge ab + bc + ca.$

Đẳng thức xảy ra khi và chỉ khi $a = b = c.$

b) Xét hiệu hai vế của bất đẳng thức:

$\left( {{a^2} + {b^2} + {c^2} + 3} \right)$ $– 2\left( {a + b + c} \right)$ $= {a^2} – 2a + 1 + {b^2} – 2b + 1 + {c^2} – 2c + 1$ $= {\left( {a – 1} \right)^2} + {\left( {b – 1} \right)^2} + {\left( {c – 1} \right)^2} \ge 0.$

Suy ra ${a^2} + {b^2} + {c^2} + 3$ $\ge 2\left( {a + b + c} \right).$

Đẳng thức xảy ra khi và chỉ khi $a = b = c = 1.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 2. Cho $a$, $b$, $c$ là các số thực bất kì. Chứng minh rẳng: $\frac{{{a}^{2}}+{{b}^{2}}+{{c}^{2}}}{3}$ $\ge {{\left( \frac{a+b+c}{3} \right)}^{2}}.$

Phân tích: Đây là một bất đẳng thức khá quen thuộc, ta có thể giải bằng cách xét hiệu vế trái và vế phải rồi phân tích thành tổng các bình phương.

Lời giải:

Xét hiệu hai vế của bất đẳng thức:

$\frac{{{a^2} + {b^2} + {c^2}}}{3}$ $– {\left( {\frac{{a + b + c}}{3}} \right)^2}$ $= \frac{{3\left( {{a^2} + {b^2} + {c^2}} \right) – {{\left( {a + b + c} \right)}^2}}}{9}$ $= \frac{{{{\left( {a – b} \right)}^2} + {{\left( {b – c} \right)}^2} + {{\left( {c – a} \right)}^2}}}{9}.$

Suy ra: $\frac{{{a^2} + {b^2} + {c^2}}}{3}$ $\ge {\left( {\frac{{a + b + c}}{3}} \right)^2}.$

Đẳng thức xảy ra khi và chỉ khi $a = b = c.$

Nhận xét: Qua hai ví dụ trên ta nhận thấy khi biến đổi tương đương bất đẳng thức bậc hai thường xuất hiện các đại lượng ${{\left( a-b \right)}^{2}}$; ${{\left( b-c \right)}^{2}}$; ${{\left( c-a \right)}^{2}}$ với điều kiện dấu đẳng thức xảy ra tại $a=b=c$. Do đó trước khi biến đổi bất đẳng thức ta nên dự đoán dấu đẳng thức xảy ra để từ đó có hướng đi hợp lí.

<!-- chunk:4 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 3. Cho $a$, $b$, $c$ là các số thực bất kì. Chứng minh rằng: ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}+{{d}^{2}}+{{e}^{2}}$ $\ge a\left( b+c+d+e \right).$

Phân tích: Bất đẳng thức cần chứng minh có hình thức tương tự như các bất đẳng thức trên, ta có thể giải bằng cách xét hiệu vế trái và vế phải rồi phân tích thành tổng các bình phương. Để được các tích $\text{ab}$, $\text{ac}$, $\text{ad}$, $\text{ae}$ vào trong bình phương ta cần ghép $a$ với $b$, $c$, $d$, $e$ và vì vai trò của $b$, $c$, $d$, $e$ như nhau nên ta có thể nghĩ đến việc biến đổi như sau:

${a^2} + {b^2} + {c^2} + {d^2} + {e^2}$ $\ge a\left( {b + c + d + e} \right)$ $\Leftrightarrow {\left( {a – kb} \right)^2} + {\left( {a – kc} \right)^2}$ $+ {\left( {a – kd} \right)^2} + {\left( {a – ke} \right)^2} \ge 0.$

Trong trường hợp trên ta có thể chọn $k=2$, tức là ta phải nhân hai vế với $4.$

Lời giải:

Xét hiệu hai vế của bất đẳng thức:

${a^2} + {b^2} + {c^2} + {d^2} + {e^2}$ $– a\left( {b + c + d + e} \right)$ $= \frac{{4\left( {{a^2} + {b^2} + {c^2} + {d^2} + {e^2}} \right) – 4\left( {ab + ac + ad + ae} \right)}}{4}$ $= \frac{{\left( {{a^2} – 4ab + 4{b^2}} \right) + \left( {{a^2} – 4ac + 4{c^2}} \right) + \left( {{a^2} – 4ad + 4{d^2}} \right) + \left( {{a^2} – 4ae + 4{e^2}} \right)}}{4}$ $= \frac{{{{\left( {a – 2b} \right)}^2} + {{\left( {a – 2c} \right)}^2} + {{\left( {a – 2d} \right)}^2} + {{\left( {a – 2e} \right)}^2}}}{4} \ge 0.$

Suy ra: ${a^2} + {b^2} + {c^2} + {d^2} + {e^2}$ $\ge a\left( {b + c + d + e} \right).$

Đẳng thức xảy ra khi và chỉ khi: $a = 2b = 2c = 2d = 2e.$

Nhận xét: Với bất đẳng thức trên, ngoài phép biến đổi tương đương ta còn có thể dùng tính chất của tam thức bậc hai để chứng minh.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 4. Cho $a$, $b$, $c$ là các số thực thỏa mãn điều kiện $a,b,c\ge 1$. Chứng minh rằng:

a) $\frac{1}{1+{{a}^{2}}}+\frac{1}{1+{{b}^{2}}}$ $\ge \frac{2}{1+ab}.$

b) $\frac{1}{1+{{a}^{3}}}+\frac{1}{1+{{b}^{3}}}+\frac{1}{1+{{c}^{3}}}$ $\ge \frac{3}{1+abc}.$

Phân tích: Để ý ta thấy, mẫu của các biểu thức xuất hiệt các bình phương, ý tưởng chứng minh bất đẳng thức trên là xét hiệu và phân tích làm xuất hiện các bình phương. Chú ý đến giả thiết $a,b\ge 1$ $\Rightarrow ab-1\ge 0.$

Lời giải:

a) Xét hiệu hai vế của bất đẳng thức:

$\frac{1}{{1 + {a^2}}} + \frac{1}{{1 + {b^2}}} – \frac{2}{{1 + ab}}$ $= \frac{1}{{1 + {a^2}}} – \frac{1}{{1 + ab}}$ $+ \frac{1}{{1 + {b^2}}} – \frac{1}{{1 + ab}}$ $= \frac{{{{\left( {a – b} \right)}^2}\left( {ab – 1} \right)}}{{\left( {{a^2} + 1} \right)\left( {{b^2} + 1} \right)\left( {ab + 1} \right)}} \ge 0.$

Suy ra $\frac{1}{{1 + {a^2}}} + \frac{1}{{1 + {b^2}}}$ $\ge \frac{2}{{1 + ab}}.$

Đẳng thức xảy ra khi và chỉ khi $a = b = 1.$

b) Bất đẳng thức cần chứng minh tương đương với: $\frac{1}{{1 + {a^3}}} + \frac{1}{{1 + {b^3}}} + \frac{1}{{1 + {c^3}}}$ $\ge \frac{3}{{1 + abc}}$ $\Leftrightarrow \frac{1}{{1 + {a^3}}} + \frac{1}{{1 + {b^3}}}$ $+ \frac{1}{{1 + {c^3}}} + \frac{1}{{1 + abc}}$ $\ge \frac{4}{{1 + abc}}.$

Áp dụng bất đẳng thức ở câu a ta được:

$\frac{1}{{1 + {a^3}}} + \frac{1}{{1 + {b^3}}}$ $+ \frac{1}{{1 + {c^3}}} + \frac{1}{{1 + abc}}$ $\ge \frac{2}{{1 + \sqrt {{a^3}{b^3}} }} + \frac{2}{{1 + \sqrt {ab{c^4}} }}$ $\ge \frac{4}{{1 + \sqrt {{a^3}{b^3}\sqrt {ab{c^4}} } }}$ $= \frac{4}{{1 + abc}}.$

Suy ra $\frac{1}{{1 + {a^3}}} + \frac{1}{{1 + {b^3}}} + \frac{1}{{1 + {c^3}}}$ $\ge \frac{3}{{1 + abc}}.$

Đẳng thức xảy ra khi và chỉ khi $a = b = c = 1.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 5. Cho $a$, $b$, $c$ là các số thực dương thỏa mãn ${{a}^{3}}+{{b}^{3}}=a-b$. Chứng minh rẳng: ${{a}^{2}}+{{b}^{2}}+ab<1.$

Phân tích: Quan sát bất đẳng thức cần chứng minh ta thấy có biểu thức ${{a}^{2}}+{{b}^{2}}+ab$. Trong khi đó giả thiết lại xuất hiện biểu thức $a-b$. Vậy mối liên hệ của hai biểu thức này như thế nào? Dễ thấy được hằng đẳng thức $\left( a-b \right)\left( {{a}^{2}}+{{b}^{2}}+ab \right)$ $={{a}^{3}}-{{b}^{3}}$. Do đó một cách rất tự nhiên ta nhân hai vế của giả thiết với biểu thức ${{a}^{2}}+{{b}^{2}}+ab$ để làm xuất hiện ${{a}^{3}}-{{b}^{3}}$ và ${{a}^{2}}+{{b}^{2}}+ab$, khi đó ta được ${{a}^{2}}+ab+{{b}^{2}}$ $=\frac{{{a}^{3}}-{{b}^{3}}}{{{a}^{3}}+{{b}^{3}}}$. Tới đây chỉ cần chứng minh $\frac{{{a}^{3}}-{{b}^{3}}}{{{a}^{3}}+{{b}^{3}}}<1$ là xong.

Lời giải:

Biến đổi giả thiết ta được:

${a^3} + {b^3} = a – b$ $\Leftrightarrow \left( {{a^3} + {b^3}} \right)\left( {{a^2} + ab + {b^2}} \right)$ $= \left( {a – b} \right)\left( {{a^2} + ab + {b^2}} \right)$ $\Leftrightarrow \left( {{a^3} + {b^3}} \right)\left( {{a^2} + ab + {b^2}} \right)$ $= {a^3} – {b^3}$ $\Leftrightarrow {a^2} + ab + {b^2}$ $= \frac{{{a^3} – {b^3}}}{{{a^3} + {b^3}}}.$

Ta cần chứng minh: $\frac{{{a^3} – {b^3}}}{{{a^3} + {b^3}}} < 1$ $\Leftrightarrow {a^3} – {b^3} < {a^3} + {b^3}$ $\Leftrightarrow 0 < 2{b^3}$ $\Leftrightarrow 0 < b.$

Do $b > 0$ hiển nhiên đúng nên bất đẳng thức được chứng minh.

<!-- chunk:7 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 6. Cho $a$, $b$ là các số thực dương thỏa mãn điều kiện $a>b$. Chứng minh rằng: $\sqrt{{{a}^{2}}-{{b}^{2}}}+\sqrt{2ab-{{b}^{2}}}>a.$

Phân tích: Bất đẳng thức có chứa căn bậc hai và các biểu thức trong căn có chứa các bình phương, lại có thêm điều kiện $a>b>0$, nên ta bình phương hai vế để biến đổi bất đẳng thức.

Lời giải:

Bất đẳng thức cần chứng minh tương đương với:

${\left( {\sqrt {{a^2} – {b^2}} + \sqrt {2ab – {b^2}} } \right)^2} > {a^2}$ $\Leftrightarrow {a^2} – {b^2}$ $+ 2\sqrt {{a^2} – {b^2}} .\sqrt {2ab – {b^2}}$ $+ 2ab – {b^2} > {a^2}$ $\Leftrightarrow 2b\left( {a – b} \right)$ $+ 2\sqrt {{a^2} – {b^2}} .\sqrt {2ab – {b^2}} > 0.$

Vì $a > b > 0$ nên $b\left( {a – b} \right) > 0.$ Vậy bất đẳng thức được chứng minh.

<!-- chunk:8 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 7. Cho các số thực $a$, $b$, $c$ thỏa mãn điều kiện $a+b+c=0$. Chứng minh rằng: $ab+2bc+3ca\le 0.$

Phân tích: Từ giả thiết $a+b+c=0$ ta có thể rút một biến theo các biến còn lại, chẳng hạn $c=-a-b$, thay vào biểu thức của bất đẳng thức ta được $3{{a}^{2}}+4ab+2{{b}^{2}}$ là biểu thức chỉ chứa hai biến và xuất hiện các bình phương. Đến đây ta tìm cách phân tích thành tổng các bình phương để chứng minh bất đẳng thức.

Lời giải:

Theo giả thiết thì $c = – \left( {a + b} \right)$, nên bất đẳng thức đã cho tương ứng với:

$ab + c\left( {2a + 3a} \right) \le 0$ $\Leftrightarrow ab + \left( { – a – b} \right)\left( {2b + 3a} \right) \le 0$ $\Leftrightarrow ab – 2ab – 3{a^2} – 2{b^2} – 3ab \le 0$ $\Leftrightarrow 3{a^2} + 4ab + 2{b^2} \ge 0$ $\Leftrightarrow {a^2} + 2{\left( {a + b} \right)^2} \ge 0.$

Từ đó suy ra điều cần chứng minh.

Dấu đẳng thức xảy ra khi và chỉ khi $a=b=c=0$.

[ads]

<!-- chunk:9 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 8. Cho $a$, $b$, $c$ là các số thực dương tùy ý. Chứng minh rằng: $\frac{{{a}^{3}}+{{b}^{3}}}{ab}+\frac{{{b}^{3}}+{{c}^{3}}}{bc}+\frac{{{c}^{3}}+{{a}^{3}}}{ca}$ $\ge 2\left( a+b+c \right).$

Phân tích: Quan sát bất đẳng thức cần chứng minh ta nhận thấy những đặc điểm sau:

+ Hai vế của bất đẳng thức cùng có bậc một.

+ Bất đẳng thức cần chứng minh làm ta liên tưởng đến một bất bất đẳng thức khá hay dùng ${{x}^{3}}+{{y}^{3}}\ge xy\left( x+y \right).$

Lời giải:

Trước hết ta chứng minh bất đẳng thức ${{x}^{3}}+{{y}^{3}}\ge xy\left( x+y \right)$ với $x$, $y$ là các số dương.

Thật vậy:

${{x}^{3}}+{{y}^{3}}$ $\ge xy\left( x+y \right)$ $\Leftrightarrow \left( x+y \right)\left( {{x}^{2}}+{{y}^{2}}-xy \right)$ $\ge xy\left( x+y \right)$ $\Leftrightarrow {{\left( x-y \right)}^{2}}\ge 0.$

Áp dụng bất đẳng thức trên ta được:

$\frac{{{a}^{3}}+{{b}^{3}}}{ab}+\frac{{{b}^{3}}+{{c}^{3}}}{bc}+\frac{{{c}^{3}}+{{a}^{3}}}{ca}$ $\ge \frac{ab\left( a+b \right)}{ab}+\frac{bc\left( b+c \right)}{bc}+\frac{ca\left( c+a \right)}{ca}$ $=2\left( a+b+c \right).$

Suy ra $\frac{{{a}^{3}}+{{b}^{3}}}{ab}+\frac{{{b}^{3}}+{{c}^{3}}}{bc}+\frac{{{c}^{3}}+{{a}^{3}}}{ca}$ $\ge 2\left( a+b+c \right).$

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 9. Chứng minh rằng với mọi số thực khác không $a$, $b$ ta có: $\frac{{{a}^{2}}}{{{b}^{2}}}+\frac{{{b}^{2}}}{{{a}^{2}}}$ $\ge \frac{a}{b}+\frac{b}{a}.$

Phân tích: Để ý ta thấy $\frac{{{a}^{2}}}{{{b}^{2}}}+\frac{{{b}^{2}}}{{{a}^{2}}}$ $={{\left( \frac{a}{b}+\frac{b}{a} \right)}^{2}}-2$, do đó ta có thể biến đổi bất đẳng thức thành ${{\left( \frac{a}{b}+\frac{b}{a} \right)}^{2}}-2-\left( \frac{a}{b}+\frac{b}{a} \right)\ge 0$. Đến đây ta có thể phân tích thành tích rồi quy đồng hoặc đặt biến phụ $t=\frac{a}{b}+\frac{b}{a}$, chú ý điều kiện $\left| t \right|\ge 2$

Lời giải:

Bất đẳng thức đã cho tương đương với:

$\frac{{{a}^{2}}}{{{b}^{2}}}+\frac{{{b}^{2}}}{{{a}^{2}}}$ $\ge \frac{a}{b}+\frac{b}{a}$ $\Leftrightarrow {{\left( \frac{a}{b}+\frac{b}{a} \right)}^{2}}-2-\left( \frac{a}{b}+\frac{b}{a} \right)\ge 0$ $\Leftrightarrow \left( \frac{a}{b}+\frac{b}{a}+1 \right)\left( \frac{a}{b}+\frac{b}{a}-2 \right)\ge 0.$

Đến đây ta có hai hướng xử lý bất đẳng thức trên.

+ Hướng 1: Biến đổi tương đương tiếp ta được bất đẳng thức: $\frac{\left( {{a}^{2}}+{{b}^{2}}+ab \right){{\left( a-b \right)}^{2}}}{{{a}^{2}}{{b}^{2}}}\ge 0.$

Mà ${{a}^{2}}+{{b}^{2}}+ab$ $=\frac{{{\left( a+b \right)}^{2}}+\left( {{a}^{2}}+{{b}^{2}} \right)}{2}\ge 0.$

Do đó bất đẳng thức được chứng minh.

+ Hướng 2: Đặt $t=\frac{a}{b}+\frac{b}{a}$, khi đó ta được ${{t}^{2}}={{\left( \frac{a}{b}+\frac{b}{a} \right)}^{2}}\ge 4$ $\Rightarrow \left| t \right|\ge 2.$

Khi đó bất đẳng thức cần chứng minh được viết lại thành $\left( t+1 \right)\left( t-2 \right)\ge 0.$

Nếu $t\ge 2$, suy ra $t-2\ge 0$ nên $\left( t+1 \right)\left( t-2 \right)\ge 0.$

Nếu $t\le -2$, suy ra $t+1<0$; $t-2<0$ nên $\left( t+1 \right)\left( t-2 \right)>0.$

Do đó bất đẳng thức được chứng minh.

Đẳng thức xảy ra khi và chỉ khi $a=b.$

<!-- chunk:11 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 10. Cho $a$, $b$ là các số thực thỏa mãn $a\ge 1$; $b\ge 1$. Chứng minh rằng: $a\sqrt{b-1}+b\sqrt{a-1}\le ab.$

Phân tích: Bất đẳng thức có chứa căn bậc hai và đẳng thức xảy ra tại $a=b=2$, do đó ta có các ý tưởng chứng minh bất đẳng thức sau đây:

+ Thứ nhất là đặt biến phụ $x=\sqrt{a-1}$; $y=\sqrt{b-1}$ để làm mất căn bậc hai và phân tích thành các bình phương.

+ Thứ hai là khử căn bậc hai bằng một đánh giá quen thuộc ${{x}^{2}}+{{y}^{2}}\ge 2xy$. Để ý đến chiều bất đẳng thức và điều kiện dấu bằng xảy ra tại $a=b=2$ ta đánh giá được:

$\sqrt{a-1}$ $\le \sqrt{\left( a-1 \right).1}$ $\le \frac{a-1+1}{2}$ $=\frac{a}{2}.$

$\sqrt{b-1}$ $=\sqrt{\left( b-1 \right).1}$ $\le \frac{b-1+1}{2}$ $=\frac{b}{2}.$

Lời giải:

Cách 1: Đặt $x=\sqrt{a-1}$; $y=\sqrt{b-1}$, khi đó $x\ge 0$; $y\ge 0$.

Bất đẳng thức cần chứng minh được viết lại thành:

$\left( {{x}^{2}}+1 \right)y+\left( {{y}^{2}}+1 \right)y$ $\le \left( {{x}^{2}}+1 \right)\left( {{y}^{2}}+1 \right)$ $\Leftrightarrow \left( {{x^2} + 1} \right)\left( {{y^2} + 1} \right) – 2\left( {{x^2} + 1} \right)y$ $+ \left( {{x^2} + 1} \right)\left( {{y^2} + 1} \right) – 2\left( {{y^2} + 1} \right)x \ge 0$ $\Leftrightarrow \left( {{x^2} + 1} \right){\left( {y – 1} \right)^2}$ $+ \left( {{y^2} + 1} \right){\left( {x – 1} \right)^2} \ge 0$ (luôn đúng).

Vậy bất đẳng thức được chứng minh.

Đẳng thức xảy ra khi và chỉ khi $x=y=1$ hay $a=b=2.$

Cách 2: Áp dụng một bất đẳng thức quen thuộc ta được:

$\sqrt {a – 1}$ $\le \sqrt {\left( {a – 1} \right).1}$ $\le \frac{{a – 1 + 1}}{2}$ $= \frac{a}{2}.$

$\sqrt {b – 1}$ $= \sqrt {\left( {b – 1} \right).1}$ $\le \frac{{b – 1 + 1}}{2}$ $= \frac{b}{2}.$

Do đó ta được $a\sqrt {b – 1} + b\sqrt {a – 1}$ $\le \frac{{ab}}{2} + \frac{{ab}}{2} = ab.$

Đẳng thức xảy ra khi và chỉ khi $a=b=2.$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 11. Cho $a$, $b$, $c$ là các số thực dương tùy ý. Chứng minh rằng:

a) $a\left( {a – b} \right)\left( {a – c} \right) + b\left( {b – c} \right)\left( {b – a} \right)$ $+ c\left( {c – a} \right)\left( {c – b} \right) \ge 0.$

b) ${a^6} + {b^6} + {c^6}$ $\ge {a^5}b + {b^5}c + {c^5}a.$

Phân tích:

a) Quan sát bất đẳng thức thứ nhất ta nhận thấy $a-c$ $=\left( a-b \right)+\left( b-c \right)$ do đó bất đẳng thức lúc này tương đương với $a{{\left( a-b \right)}^{2}}$ $+c\left( a-c \right)\left( b-c \right)\ge 0$. Đến đây chỉ cần sắp thứ tự các biến sao cho $c\left( a-c \right)\left( b-c \right)\ge 0$ là xong.

b) Tương tự như trên ta có $a-c=\left( a-b \right)+\left( b-c \right)$, biến đổi tương đương bất đẳng thức ta được bất đẳng thức $\left( a-b \right)\left( {{a}^{5}}-{{b}^{5}} \right)$ $+\left( a-c \right)\left( {{b}^{5}}-{{c}^{5}} \right)\ge 0$. Đến đây ta chỉ cần sắp thứ tự các biến sao cho $\left( a-c \right)\left( {{b}^{5}}-{{c}^{5}} \right)\ge 0$ là xong.

Lời giải:

a) Vì vai trò của $a$, $b$, $c$ trong bất đẳng thức như nhau nên không mất tính tổng quát ta giả sử $a\ge b\ge c\ge 0$. Khi đó ta có:

$a\left( {a – b} \right)\left( {a – c} \right) + a\left( {b – c} \right)\left( {b – a} \right)$ $+ c\left( {c – a} \right)\left( {c – b} \right) \ge 0$

$\Leftrightarrow a\left( {a – b} \right)\left[ {\left( {a – b} \right) + \left( {b – c} \right)} \right]$ $+ b\left( {b – c} \right)\left( {b – a} \right) + c\left( {c – a} \right)\left( {c – b} \right) \ge 0$

$\Leftrightarrow a{\left( {a – b} \right)^2} + a\left( {a – b} \right)\left( {b – c} \right)$ $– a\left( {b – c} \right)\left( {a – b} \right) + c\left( {a – c} \right)\left( {b – c} \right) \ge 0$

$\Leftrightarrow {\left( {a – b} \right)^2}\left( {a + b – c} \right)$ $+ c\left( {a – c} \right)\left( {b – c} \right) \ge 0$ (luôn đúng vì $a\ge b\ge c\ge 0$).

Vậy bất đẳng thức được chứng minh.

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$

b) Vì vai trò của $a$, $b$, $c$ trong bất đẳng thức như nhau nên không mất tính tổng quát ta giả sử $a\ge c\ge 0;b\ge c\ge 0$. Khi đó ta có:

${a^6} – {a^5}b + {b^6} – {b^5}c + {c^6} – {c^5}a \ge 0$ $\Leftrightarrow {a^5}\left( {a – b} \right) + {b^5}\left( {b – c} \right) + {c^5}\left( {c – a} \right) \ge 0$ $\Leftrightarrow {a^5}\left( {a – b} \right) – {b^5}\left[ {\left( {a – b} \right) + \left( {c – a} \right)} \right]$ $+ {c^5}\left( {c – a} \right) \ge 0$ $\Leftrightarrow \left( {a – b} \right)\left( {{a^5} – {b^5}} \right)$ $+ \left( {a – c} \right)\left( {{b^5} – {c^5}} \right) \ge 0.$ (luôn đúng vì $a\ge c\ge 0$; $b\ge c\ge 0$).

Vậy bất đẳng thức được chứng minh.

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$

<!-- chunk:13 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 12. Cho $a$, $b$, $c$ là các số thực dương tùy ý. Chứng minh rằng: $\frac{{{a}^{2}}}{b}+\frac{{{b}^{2}}}{c}+\frac{{{c}^{2}}}{a}$ $\ge a+b+c.$

Phân tích: Nhận thấy $\frac{{{a}^{2}}}{b}-2a+b$ $=\frac{{{\left( a-b \right)}^{2}}}{b}$. Áp dụng tương tự ta được bất đẳng thức cần chứng minh.

Lời giải:

Bất đẳng thức cần chứng minh tương đương với:

$\left( {\frac{{{a^2}}}{b} – 2a + b} \right) + \left( {\frac{{{b^2}}}{c} – 2b + c} \right)$ $+ \left( {\frac{{{c^2}}}{a} – 2c + a} \right) \ge 0$

$\Leftrightarrow \frac{{{a^2} – 2ab + {b^2}}}{b} + \frac{{{b^2} – 2bc + {c^2}}}{c}$ $+ \frac{{{c^2} – 2ca + {a^2}}}{a} \ge 0$

$\Leftrightarrow \frac{{{{\left( {a – b} \right)}^2}}}{b} + \frac{{{{\left( {b – c} \right)}^2}}}{c}$ $+ \frac{{{{\left( {c – a} \right)}^2}}}{a} \ge 0$ (luôn đúng vì $a$, $b$, $c$ là các số thực dương).

Vậy bất đẳng thức được chứng minh.

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$

<!-- chunk:14 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 13. Cho $a$, $b$, $c$ là độ dài ba cạnh của một tam giác. Chứng minh rằng:

a) ${a^2} + {b^2} + {c^2}$ $< 2\left( {ab + bc + ca} \right).$

b) $abc$ $\ge \left( {a + b – c} \right)\left( {b + c – a} \right)\left( {c + a – b} \right).$

a) Vì $a$, $b$, $c$ là độ dài ba cạnh của một tam giác nên ta có:
\left\{ \begin{matrix}
0<a<b+c \\
0<b<a+c \\
0<c<a+b \\
\end{matrix} \right.
$$
 
$$
\Rightarrow \left\{ \begin{matrix}
{{a}^{2}}<a(b+c) \\
{{b}^{2}}<b(a+c) \\
{{c}^{2}}<c(a+b) \\
\end{matrix} \right.
Cộng theo vế ba bất đẳng thức trên ta được ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}$ $<2\left( ab+bc+ca \right).$

b) Vì $a$, $b$, $c$ là độ dài ba cạnh của một tam giác nên ta có:

${{a}^{2}}\ge {{a}^{2}}-{{\left( b-c \right)}^{2}}$ $=\left( a-b+c \right)\left( a+b-c \right)>0.$

Chứng minh tương tự ta được: ${{b}^{2}}\ge {{b}^{2}}-{{(c-a)}^{2}}>0$; ${{c}^{2}}\ge {{c}^{2}}-{{(a-b)}^{2}}>0.$

Nhân vế các bất đẳng thức ta được: ${a^2}{b^2}{c^2}$ $\ge \left[ {{a^2} – {{\left( {b – c} \right)}^2}} \right]\left[ {{b^2} – {{\left( {c – a} \right)}^2}} \right]\left[ {{c^2} – {{\left( {a – b} \right)}^2}} \right].$

Suy ra: ${a^2}{b^2}{c^2}$ $\ge {\left( {a + b – c} \right)^2}{\left( {b + c – a} \right)^2}{\left( {c + a – b} \right)^2}.$

Mà ta lại có $a+b-c>0$; $b+c-a>0$; $c+a-b>0.$

Nên từ bất đẳng thức trên ta được $abc$ $\ge \left( a+b-c \right)\left( b+c-a \right)\left( c+a-b \right).$

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$
Nhận xét: Bất đẳng thức $abc$ $\ge \left( a+b-c \right)\left( b+c-a \right)\left( c+a-b \right)$ không chỉ đúng với $a$, $b$, $c$ là các cạnh của một tam giác, mà nó còn đúng cho $a$, $b$, $c$ là các số thực dương bất kì. Bất đẳng này là một trường hợp của bất đẳng thức Schur.

<!-- chunk:15 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 14. Cho các số thực $a,b,c\in [0;2]$ và $a+b+c=3$. Chứng minh rằng: $3\le {{a}^{2}}+{{b}^{2}}+{{c}^{2}}\le 5.$

Đặt $x=a+1$; $y=b+1$; $z=c+1$, khi đó ta được $x,y,z\in [-1,1]$ và $x+y+z=0.$

Ta có: ${a^2} + {b^2} + {c^2}$ $= {\left( {x + 1} \right)^2} + {\left( {y + 1} \right)^2} + {\left( {z + 1} \right)^2}$ $= {x^2} + {y^2} + {z^2} + 2\left( {x + y + z} \right) + 3$ $= {x^2} + {y^2} + {z^2} + 3 \ge 3.$

Dấu đẳng thức có khi $x=y=z=0$ hay $a=b=c=1.$

Mặt khác do $x,y,z\in [-1,1]$ nên ta có: $\left( {1 – x} \right)\left( {1 – y} \right)\left( {1 – z} \right)$ $+ \left( {1 + x} \right)\left( {1 + y} \right)\left( {1 + z} \right) \ge 0$ $\Leftrightarrow 2 + 2\left( {xy + {\rm{yx}} + zx} \right) \ge 0$ $\Leftrightarrow 2 – \left( {{x^2} + {y^2} + {z^2}} \right)$ $+ {\left( {x + y + x} \right)^2} \ge 0$ $\Leftrightarrow {x^2} + {y^2} + {z^2} \le 2.$

<!-- chunk:16 level:3 source:https://toanmath.com/2018/09/chung-minh-bat-dang-thuc-bang-phuong-phap-bien-doi-tuong-duong.html -->
## Ví dụ 15. Cho $a$, $b$, $c$ là các số thực dương tùy ý. Chứng minh rằng: $\frac{a}{b+c}+\frac{b}{c+a}+\frac{c}{a+b}\ge \frac{3}{2}.$

Phân tích: Bất đẳng thức cần chứng minh là bất đẳng thức Neibizt nổi tiếng, hiện nay có rất nhiều cách chứng minh cho bất đẳng thức này. Để chứng minh bằng phương pháp biến đổi tương đương ta có các ý tưởng như sau:

+ Thứ nhất ta xét hiệu hai vế và chú ý $\frac{a}{b+c}-\frac{1}{2}$ $=\frac{a-b}{2\left( b+c \right)}+\frac{a-c}{2\left( b+c \right)}$, khi đó ta có $6$ phân thức. Dự đoán dấu đẳng thức xảy ra khi $a=b=c$, nên ta ghép hai phân thức làm một nhóm sao cho có thể phân tích được thành bình phương của hiệu hai trong ba số $a$, $b$, $c$. Để ý là: $\frac{a-b}{b+c}-\frac{a-b}{c+a}$ $=\frac{{{\left( a-b \right)}^{2}}}{\left( b+c \right)\left( c+a \right)}.$

+ Thứ hai ta để ý đến biến đổi $\frac{a}{b+c}+1$ $=\frac{a+b+c}{b+c}$. Do đó ta cộng vào hai vế của bất đẳng thức với $3$, thực hiện biến đổi như trên ta đưa được bất đẳng thức về dạng như sau $\left( 2a+2b+2c \right)\left( \frac{1}{b+c}+\frac{1}{c+a}+\frac{1}{a+b} \right)\ge 9$, đến đây ta có thể đơn giản hóa bất đẳng thức bằng việc đặt biến phụ $x=b+c$; $y=c+a$; $z=a+b.$

+ Thứ ba là ta tiến hành đặt biến phụ $x=b+c$; $y=c+a$; $z=a+b$ ngay từ đầu, khi đó ta được $a=\frac{y+z-x}{2}$; $b=\frac{z+x-y}{2}$; $c=\frac{x+y-z}{2}$ và bất đẳng thức cần chứng minh thu được ở đây là $\frac{y+z-x}{x}+\frac{z+x-y}{y}+\frac{x+y-z}{z}\ge 3$ sẽ chứng minh dễ dàng hơn.

Lời giải:

Cách 1: Bất đẳng thức cần chứng minh tương đương với:

$\frac{a}{{b + c}} – \frac{1}{2} + \frac{b}{{c + a}}$ $– \frac{1}{2} + \frac{c}{{a + b}} – \frac{1}{2} \ge 0$

$\Leftrightarrow \frac{{a – b}}{{b + c}} + \frac{{a – c}}{{b + c}} + \frac{{b – c}}{{c + a}}$ $+ \frac{{b – a}}{{c + a}} + \frac{{c – a}}{{a + b}} + \frac{{c – b}}{{a + b}} \ge 0$

$\Leftrightarrow \left( {\frac{{a – b}}{{b + c}} – \frac{{a – b}}{{c + a}}} \right) + \left( {\frac{{b – c}}{{c + a}} – \frac{{b – c}}{{a + b}}} \right)$ $+ \left( {\frac{{c – a}}{{a + b}} – \frac{{c – a}}{{b + c}}} \right) \ge 0$

$\Leftrightarrow \frac{{{{\left( {a – b} \right)}^2}}}{{\left( {b + c} \right)\left( {c + a} \right)}} + \frac{{{{\left( {b – c} \right)}^2}}}{{\left( {c + a} \right)\left( {a + b} \right)}}$ $+ \frac{{{{\left( {c – b} \right)}^2}}}{{\left( {a + b} \right)\left( {b + c} \right)}} \ge 0.$

Vậy bất đẳng thức được chứng minh.

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$

Cách 2: Bất đẳng thứ cần chứng minh tương đương với:

$\frac{a}{{b + c}} + \frac{1}{2} + \frac{b}{{c + a}}$ $+ \frac{1}{2} + \frac{c}{{a + b}} + \frac{1}{2} \ge \frac{9}{2}$ $\Leftrightarrow \left( {2a + 2b + 2c} \right)$$\left( {\frac{1}{{b + c}} + \frac{1}{{c + a}} + \frac{1}{{a + b}}} \right) \ge 9.$

Đặt $x=b+c$; $y=c+a$; $z=a+b$ khi đó bất đẳng thức cần chứng minh trở thành:

$\left( {x + y + z} \right)\left( {\frac{1}{x} + \frac{1}{y} + \frac{1}{z}} \right) \ge 9$ $\Leftrightarrow \frac{x}{y} + \frac{y}{x} + \frac{y}{z} + \frac{z}{x} + \frac{z}{x} + \frac{x}{z} \ge 6$

$\Leftrightarrow \left( {\frac{x}{y} + \frac{y}{x} – 2} \right) + \left( {\frac{y}{z} + \frac{z}{y} – 2} \right)$ $+ \left( {\frac{x}{z} + \frac{z}{x} – 2} \right) \ge 0$

$\Leftrightarrow \frac{{{{\left( {x – y} \right)}^2}}}{{2xy}} + \frac{{{{\left( {y – z} \right)}^2}}}{{2yz}}$ $+ \frac{{{{\left( {z – x} \right)}^2}}}{{2zx}} \ge 0$

Vậy bất đẳng thức được chứng minh.

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$

Cách 3: Đặt $x=b+c$; $y=c+a$; $z=a+b$, khi đó ta được: $a=\frac{y+z-x}{2}$; $b=\frac{z+x-y}{2}$; $c=\frac{x+y-z}{2}.$

Bất đẳng thức cần chứng minh trở thành:

$\frac{{y + z – x}}{x} + \frac{{z + x – y}}{y}$ $+ \frac{{x + y – z}}{z} \ge 3$ $\Leftrightarrow \left( {\frac{x}{y} + \frac{y}{x} – 2} \right) + \left( {\frac{y}{z} + \frac{z}{y} – 2} \right)$ $+ \left( {\frac{x}{z} + \frac{z}{x} – 2} \right) \ge 0$ $\Leftrightarrow \frac{{{{\left( {x – y} \right)}^2}}}{{2xy}} + \frac{{{{\left( {y – z} \right)}^2}}}{{2yz}}$ $+ \frac{{{{\left( {z – x} \right)}^2}}}{{2zx}} \ge 0.$

Vậy bất đẳng thức được chứng minh.

Đẳng thức xảy ra khi và chỉ khi $a=b=c.$