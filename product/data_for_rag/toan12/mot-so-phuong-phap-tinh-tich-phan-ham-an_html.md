# Một số phương pháp tính tích phân hàm ẩn

<!-- chunk:0 level:0 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
Tích phân hàm ẩn là dạng toán tính tích phân trong đó hàm số cần tính tích phân không được cho dưới dạng tường minh bằng công thức, mà thông qua một số tính chất của hàm số đó, đây là dạng tích phân khó (vận dụng cao), ít được đề cập trong sách giáo khoa Giải tích 12, nhưng lại xuất hiện tương đối nhiều trong các đề thi trắc nghiệm hiện nay, chính vì vậy đã gây ra những khó khăn cho học sinh trong việc tiếp cận và giải quyết dạng toán này. Thông qua bài viết, TOANMATH.com giới thiệu đến đọc giả một số phương pháp giải bài toán tích phân hàm ẩn.

Bài viết đề cập đến bốn phương pháp tính tích phân hàm ẩn thường được sử dụng:

+ Phương pháp 1. Biến đổi đưa về nguyên hàm cơ bản.

+ Phương pháp 2. Phương pháp đổi biến số.

+ Phương pháp 3. Phương pháp tính tích phân từng phần.

+ Phương pháp 4. Tạo bình phương cho hàm số dưới dấu tích phân.

Sau đây chúng ta sẽ lần lượt tìm hiểu kỹ thuật sử dụng của từng phương pháp kể trên.

PHƯƠNG PHÁP 1. BIẾN ĐỔI ĐƯA VỀ NGUYÊN HÀM CƠ BẢN.

a. Kiến thức sử dụng
+ Nếu $F'(x) = f(x)$ với mọi $x \in K$ thì $F(x) = \int f (x)dx.$

+ Các công thức về đạo hàm cần ghi nhớ:

$u’v + uv’ = (uv)’.$

$\frac{{u’v – uv’}}{{{v^2}}} = \left( {\frac{u}{v}} \right)’.$

$\frac{{u’}}{{2\sqrt u }} = \left( {\sqrt u } \right)’.$

$n{u^{n – 1}}u’ = \left( {{u^n}} \right)’.$

$– \frac{{u’}}{{{u^2}}} = \left( {\frac{1}{u}} \right)’.$

b. Ví dụ áp dụng

<!-- chunk:1 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 1. Cho hàm số $f(x) \ne 0$ liên tục trên đoạn $[1;2]$ và thỏa mãn $f(1) = \frac{1}{3}$, ${x^2}.f'(x) = \left( {1 – 2{x^2}} \right).{f^2}(x)$ với mọi $x \in [1;2].$ Tính tích phân $I = \int_1^2 f (x)dx.$

Nhận xét: Từ giả thiết ta có $\frac{{f'(x)}}{{{f^2}(x)}} = \frac{{1 – 2{x^2}}}{{{x^2}}}$, biểu thức vế trái có dạng $\frac{{u’}}{{{u^2}}} = \left( { – \frac{1}{u}} \right)’.$ Từ đó ta có lời giải.

Lời giải: Ta có ${x^2}.f'(x) = \left( {1 – 2{x^2}} \right).{f^2}(x)$ $\Leftrightarrow \frac{{f'(x)}}{{{f^2}(x)}} = \frac{{1 – 2{x^2}}}{{{x^2}}}$ $\Leftrightarrow \left( { – \frac{1}{{f(x)}}} \right)’ = \frac{1}{{{x^2}}} – 2.$

$\Rightarrow – \frac{1}{{f(x)}} = \int {\left( {\frac{1}{{{x^2}}} – 2} \right)} dx$ $\Leftrightarrow – \frac{1}{{f(x)}} = – \frac{1}{x} – 2x + c.$

Do $f(1) = \frac{1}{3}$ $\Rightarrow c = 0.$

Nên ta có: $\frac{1}{{f(x)}} = \frac{{2{x^2} + 1}}{x}$ $\Leftrightarrow f(x) = \frac{x}{{2{x^2} + 1}}.$

Khi đó $I = \int_1^2 f (x)dx$ $= \int_1^2 {\frac{x}{{1 + 2{x^2}}}} dx$ $= \frac{1}{4}\int_1^2 {\frac{{d\left( {1 + 2{x^2}} \right)}}{{1 + 2{x^2}}}}$ $= \left. {\frac{1}{4}\ln \left| {1 + 2{x^2}} \right|} \right|_1^2$ $= \frac{1}{4}(2\ln 3 – \ln 3)$ $= \frac{1}{4}\ln 3.$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 2. Cho hàm số $f(x)$ liên tục, không âm trên $R$ và thỏa mãn $f(x).f'(x) – 2x.\sqrt {{f^2}(x) + 1} = 0$ với mọi $x \in R$ và $f(0)=0.$ Tính tích phân $I = \int_0^1 f (x)dx.$

Nhận xét: Từ giả thiết ta có $\frac{{f(x).f'(x)}}{{\sqrt {{f^2}(x) + 1} }} = 2x$, biểu thức vế trái có dạng $\frac{{uu’}}{{\sqrt {{u^2} + 1} }} = \left( {\sqrt {{u^2} + 1} } \right)’.$ Từ đó ta có lời giải.

Lời giải: Ta có $f(x).f'(x) – 2x.\sqrt {{f^2}(x) + 1} = 0$ $\Leftrightarrow \frac{{f(x).f'(x)}}{{\sqrt {{f^2}(x) + 1} }} = 2x$ $\Leftrightarrow \left( {\sqrt {{f^2}(x) + 1} } \right)’ = 2x.$

$\Rightarrow \sqrt {{f^2}(x) + 1}$ $= \int 2 xdx$ $\Leftrightarrow \sqrt {{f^2}(x) + 1} = {x^2} + c.$

Do $f(0) = 0$ $\Rightarrow c = 1$ nên ta có:

$\sqrt {{f^2}(x) + 1} = {x^2} + 1$ $\Leftrightarrow {f^2}(x) + 1 = {\left( {{x^2} + 1} \right)^2}$ $\Leftrightarrow {f^2}(x) = {x^2}\left( {{x^2} + 2} \right)$ $\Leftrightarrow f(x) = |x|\sqrt {{x^2} + 2}$ (vì $f(x)$ không âm trên $R$).

Khi đó $I = \int_0^1 f (x)dx$ $= \int_0^1 | x|\sqrt {{x^2} + 2} dx$ $= \int_0^1 x \sqrt {{x^2} + 2} dx$ $= \frac{1}{2}\int_0^1 {\sqrt {{x^2} + 2} } d\left( {{x^2} + 2} \right)$ $= \left. {\frac{1}{2}.\frac{2}{3}\left[ {\left( {{x^2} + 2} \right)\sqrt {{x^2} + 2} } \right]} \right|_0^1$ $= \frac{1}{3}(3\sqrt 3 – 2\sqrt 2 ).$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 3. Cho hàm số $f(x)$ đồng biến, có đạo hàm trên đoạn $[1;4]$ và thoả mãn $x + 2x.f(x) = {\left[ {f'(x)} \right]^2}$ với mọi $x \in [1;4].$ Biết $f(1) = \frac{3}{2}$, tính $I = \int_1^4 f (x)dx.$

Lời giải: Do $f(x)$ đồng biến trên đoạn $[1;4]$ $\Rightarrow f'(x) \ge 0$, $\forall x \in [1;4].$

Ta có $x + 2x.f(x) = {\left[ {f'(x)} \right]^2}$ $\Leftrightarrow x(1 + 2.f(x)) = {\left[ {f'(x)} \right]^2}$, do $x \in [1;4]$ và $f'(x) \ge 0$, $\forall x \in [1;4].$

$\Rightarrow f(x) > \frac{{ – 1}}{2}$ và $f'(x) = \sqrt x .\sqrt {1 + 2f(x)}$ $\Leftrightarrow \frac{{f'(x)}}{{\sqrt {1 + 2f(x)} }} = \sqrt x$ $\Leftrightarrow \left( {\sqrt {1 + 2f(x)} } \right)’ = \sqrt x .$

$\Rightarrow \sqrt {1 + 2f(x)} = \int {\sqrt x } dx$ $\Leftrightarrow \sqrt {1 + 2f(x)} = \frac{2}{3}x\sqrt x + c.$

Vì $f(1) = \frac{3}{2}$ $\Rightarrow \sqrt {1 + 2.\frac{3}{2}} = \frac{2}{3} + c$ $\Leftrightarrow c = \frac{4}{3}.$

$\Rightarrow \sqrt {1 + 2f(x)} = \frac{2}{3}x\sqrt x + \frac{4}{3}$ $\Leftrightarrow 1 + 2f(x) = {\left( {\frac{2}{3}x\sqrt x + \frac{4}{3}} \right)^2}$ $\Leftrightarrow f(x) = \frac{2}{9}{x^3} + \frac{8}{9}{x^{\frac{3}{2}}} + \frac{7}{{18}}.$

Khi đó $I = \int_1^4 f (x)dx$ $= \int_1^4 {\left( {\frac{2}{9}{x^3} + \frac{8}{9}{x^{\frac{3}{2}}} + \frac{7}{{18}}} \right)} dx$ $= \left. {\left( {\frac{1}{{18}}{x^4} + \frac{{16}}{{45}}{x^{\frac{5}{2}}} + \frac{7}{{18}}x} \right)} \right|_1^4$ $= \frac{{1186}}{{45}}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 4. Cho hàm số $f(x)$ đồng biến, có đạo hàm cấp hai trên đoạn $[0;2]$ và thỏa mãn $2{\left[ {f(x)} \right]^2} – f(x).f”(x) + {\left[ {f'(x)} \right]^2} = 0$ với mọi $x \in [0;2].$ Biết $f(0) = 1$, $f(2) = {e^6}$, tính tích phân $I = \int_{ – 2}^0 {(2x + 1)} .f(x)dx.$

Nhận xét: Từ giả thiết ta có $\frac{{f(x).f”(x) – {{\left[ {f'(x)} \right]}^2}}}{{{{[f(x)]}^2}}} = 2$, biểu thức vế trái có dạng $\left[ {\frac{{f'(x)}}{{f(x)}}} \right]’$, từ đó ta có lời giải.

Lời giải: Do $f(x)$ đồng biến trên đoạn $[0;2]$ nên ta có $f(0) \le f(x) \le f(2)$ $\Leftrightarrow 1 \le f(x) \le {e^6}.$

Ta có $2{[f(x)]^2} – f(x).f”(x) + {\left[ {f'(x)} \right]^2} = 0$ $\Leftrightarrow \frac{{f(x).f”(x) – {{\left[ {f'(x)} \right]}^2}}}{{{{[f(x)]}^2}}} = 2$ $\Leftrightarrow \left[ {\frac{{f'(x)}}{{f(x)}}} \right]’ = 2.$

$\Rightarrow \frac{{f'(x)}}{{f(x)}} = \int 2 dx$ $= 2x + c$ $\Rightarrow \int {\frac{{f'(x)}}{{f(x)}}} dx = \int {(2x + c)} dx$ $\Rightarrow \ln |f(x)| = {x^2} + cx + {c_1}.$

Mà $1 \le f(x) \le {e^6}$ nên ta có $\ln f(x) = {x^2} + cx + {c_1}.$

Do 
$$
\left\{ {\begin{array}{l}
{f(0) = 1}\\
{f(2) = {e^6}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{{c_1} = 0}\\
{4 + 2c + {c_1} = 6}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{c = 1}\\
{{c_1} = 0}
\end{array}} \right..
$$

$\Rightarrow \ln f(x) = {x^2} + x$ $\Leftrightarrow f(x) = {e^{{x^2} + x}}.$

Khi đó $I = \int_{ – 2}^0 {(2x + 1)} .f(x)dx$ $= \int_{ – 2}^0 {(2x + 1)} .{e^{{x^2} + x}}dx$ $= \int_{ – 2}^0 {{e^{{x^2} + x}}} d\left( {{e^{{x^2} + x}}} \right)$ $= \left. {{e^{{x^2} + x}}} \right|_{ – 2}^0$ $= 1 – {e^2}.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 5. Cho $f(x)$ có đạo hàm trên $R$ và thỏa mãn $3f'(x).{e^{{f^3}(x) – {x^2} – 1}} – \frac{{2x}}{{{f^2}(x)}} = 0$ với mọi $x \in R.$ Biết $f(0) = 1$, tính tích phân $I = \int_0^{\sqrt 7 } x .f(x)dx.$

Lời giải: Ta có $3f'(x).{e^{{f^3}(x) – {x^2} – 1}} – \frac{{2x}}{{{f^2}(x)}} = 0$ $\Leftrightarrow 3f'(x).{f^2}(x).{e^{{f^3}(x)}} = 2x.{e^{{x^2} + 1}}$ $\Leftrightarrow \left[ {{e^{{f^3}(x)}}} \right]’ = 2x.{e^{{x^2} + 1}}.$

$\Rightarrow {e^{{f^3}(x)}} = \int 2 x{e^{{x^2} + 1}}dx$ $= \int {{e^{{x^2} + 1}}} d\left( {{x^2} + 1} \right)$ $= {e^{{x^2} + 1}} + c.$

Do $f(0) = 1$ $\Leftrightarrow e = e + c$ $\Leftrightarrow c = 0$ $\Rightarrow {e^{{f^3}(x)}} = {e^{{x^2} + 1}}$ $\Leftrightarrow {f^3}(x) = {x^2} + 1$ $\Leftrightarrow f(x) = \sqrt[3]{{{x^2} + 1}}.$

Khi đó $I = \int_0^{\sqrt 7 } x .f(x)dx$ $= \int_0^{\sqrt 7 } x .\sqrt[3]{{{x^2} + 1}}dx$ $= \frac{1}{2}\int_0^{\sqrt 7 } {\sqrt[3]{{{x^2} + 1}}} d\left( {{x^2} + 1} \right)$ $= \left. {\frac{3}{8}\left[ {\left( {{x^2} + 1} \right)\sqrt[3]{{{x^2} + 1}}} \right]} \right|_0^{\sqrt 7 }$ $= \frac{{45}}{8}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 6. Cho $f(x)$ có đạo hàm trên $[0;1]$ thỏa mãn $f(x) + (x + 1).f'(x) = 1$ với mọi $x \in [0;1].$ Biết $f(5) = \frac{7}{6}$, tính tích phân $I = \int_0^1 f (x)dx.$

Nhận xét: Từ giả thiết ta có $(x + 1)’f(x) + (x + 1)f'(x) = 1$, vế trái là biểu thức có dạng $u’.v + u.v’ = (uv)’$, từ đó ta có lời giải.

Lời giải: Ta có $f(x) + (x + 1).f'(x) = 1$ $\Leftrightarrow (x + 1)’f(x) + (x + 1)f'(x) = 1$ $\Leftrightarrow [(x + 1)f(x)]’ = 1.$

$\Rightarrow (x + 1)f(x) = \int d x$ $\Leftrightarrow (x + 1)f(x) = x + c.$

Vì $f(5) = \frac{7}{6}$ $\Leftrightarrow 6.\frac{7}{6} = 5 + c$ $\Leftrightarrow c = 2.$

$\Rightarrow (x + 1)f(x) = x + 2$ $\Leftrightarrow f(x) = \frac{{x + 2}}{{x + 1}}.$

Khi đó $I = \int_0^1 f (x)dx$ $= \int_0^1 {\frac{{x + 2}}{{x + 1}}} dx$ $= \int_0^1 {\left( {1 + \frac{1}{{x + 1}}} \right)} dx$ $= \left. {(x + \ln |x + 1|)} \right|_0^1$ $= 1 + \ln 2.$

Nhận xét: Với $u(x)$ là biểu thức cho trước thì ta có $[u(x).f(x)]’ = u'(x).f(x) + u(x).f'(x).$ Đặt $v(x) = u'(x)$ ta được $[u(x).f(x)]’ = v(x).f(x) + u(x).f'(x)$ $(*).$ Như vậy nếu biểu thức có dạng $v(x).f(x) + u(x).f'(x)$ ta có thể biến đổi đưa về dạng $[u(x).f(x)]’.$ Khi đó ta có bài toán tổng quát cho ví dụ 6 như sau:

Cho $A(x)$, $B(x)$, $g(x)$ là các biểu thức đã biết. Tìm hàm số $f(x)$ thỏa mãn: $A(x)f(x) + B(x)f'(x) = g(x)$ $(**).$

Do vế trái có dạng $(*)$ nên ta có thể biến đổi $(**)$ $[u(x).f(x)]’ = g(x).$

Trong đó $u(x)$ được chọn sao cho: 
$$
\left\{ {\begin{array}{l}
{u'(x) = A(x)}\\
{u(x) = B(x)}
\end{array}} \right.
$$
 $\Rightarrow \frac{{u'(x)}}{{u(x)}} = \frac{{A(x)}}{{B(x)}}$ $\Rightarrow \int {\frac{{u'(x)}}{{u(x)}}} dx$ $= \int {\frac{{A(x)}}{{B(x)}}} dx.$

Suy ra $\ln |u(x)| = G(x) + c$ với $G(x)$ là một nguyên hàm của $\frac{{A(x)}}{{B(x)}}$, từ đây ta sẽ chọn được biểu thức $u(x).$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 7. Cho $f(x)$ có đạo hàm trên $[0;1]$ thỏa mãn $f(1) = \frac{1}{{2018}}$ và $2018f(x) + xf'(x) = 2{x^{2018}}$ với mọi $x \in [0;1].$ Tính tích phân $I = \int_0^1 f (x)dx.$

Nhận xét: Trước hết ta đi tìm biểu thức $u(x).$ Ta có:

$\Rightarrow \ln |u(x)| = \int {\frac{{2018}}{x}} dx$ $\Rightarrow \ln |u(x)| = 2018\ln |x| + c$ $\Leftrightarrow \ln |u(x)| = \ln {x^{2018}} + c$ nên ta chọn $u(x) = {x^{2018}}$, khi đó ta có lời giải như sau:

Lời giải: Ta có $\left[ {{x^{2018}}.f(x)} \right]’$ $= 2018{x^{2017}}f(x) + {x^{2018}}f'(x)$ $= {x^{2017}}\left[ {2018f(x) + xf'(x)} \right]$ $= {x^{2017}}.\left[ {2{x^{2018}}} \right]$ $= 2{x^{4035}}.$

Khi đó ${x^{2018}}f(x) = \int 2 {x^{4035}}dx$ $\Leftrightarrow {x^{2018}}f(x) = \frac{{{x^{4036}}}}{{2018}} + c.$

Do $f(1) = \frac{1}{{2018}}$ $\Leftrightarrow \frac{1}{{2018}} = \frac{1}{{2018}} + c.$

$\Leftrightarrow c = 0$ $\Rightarrow {x^{2018}}f(x) = \frac{{{x^{4036}}}}{{2018}}$ $\Rightarrow f(x) = \frac{{{x^{2018}}}}{{2018}}.$

Khi đó $I = \int_0^1 f (x)dx$ $= \int_0^1 {\frac{{{x^{2018}}}}{{2018}}} dx$ $= \left. {\left( {\frac{{{x^{2019}}}}{{2019.2018}}} \right)} \right|_0^1$ $= \frac{1}{{2018.2019}}.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 8. Cho $f(x)$ có đạo hàm trên $[1;2]$ thỏa mãn $(x + 1)f(x) + xf'(x) = 2{e^x}$ với mọi $x \in [1;2].$ Biết $f(1) = e$, tính tích phân $I = \int_1^2 x f(x)dx.$

Nhận xét: Trước hết ta đi tìm biểu thức $u(x).$ Ta có:

$\ln |u(x)| = \int {\frac{{x + 1}}{x}} dx$ $\Rightarrow \ln |u(x)| = x + \ln |x| + c$ $\Leftrightarrow \ln |u(x)| = \ln {e^x} + \ln |x| + c$ $\Leftrightarrow \ln |u(x)| = \ln \left| {x{e^x}} \right| + c$ nên ta chọn $u(x) = x{e^x}$, từ đó ta có lời giải.

Lời giải: Ta có $\left[ {x{e^x}f(x)} \right]’$ $= \left( {x{e^x}} \right)’f(x) + x{e^x}f'(x)$ $= \left( {{e^x} + x{e^x}} \right)f(x) + x{e^x}f'(x).$

$= {e^x}\left[ {(x + 1)f(x) + xf'(x)} \right]$ $\Rightarrow \left[ {x{e^x}f(x)} \right]’ = {e^x}\left[ {2{e^x}} \right]$ $\Rightarrow x{e^x}f(x) = \int 2 {e^{2x}}dx$ $\Leftrightarrow x{e^x}f(x) = {e^{2x}} + c.$

Do $f(1) = e$ $\Leftrightarrow e.e = {e^2} + c$ $\Leftrightarrow c = 0$ $\Rightarrow x{e^x}f(x) = {e^{2x}}$ $\Leftrightarrow f(x) = \frac{{{e^x}}}{x}.$

Khi đó $I = \int_1^2 x f(x)dx$ $= \int_1^2 {{e^x}} dx = \left. {{e^x}} \right|_1^2$ $= {e^2} – e.$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 9. Cho $f(x)$ liên tục và có đạo hàm trên $R\backslash \{ – 1;0\}$ thỏa mãn $x(x + 1)f'(x) + f(x) = {x^2} + x$ với mọi $x \in R\backslash \{ – 1;0\}$ và $f(1) = – 2\ln 2.$ Tính tích phân $\int_1^2 x f(x)dx.$

Nhận xét: Trước hết ta đi tìm biểu thức $u(x).$ Ta có:

$\ln |u(x)| = \int {\frac{1}{{x(x + 1)}}} dx$ $\Rightarrow \ln |u(x)| = \int {\left( {\frac{1}{x} – \frac{1}{{x + 1}}} \right)} dx$ $\Leftrightarrow \ln |u(x)| = \left| {\frac{x}{{x + 1}}} \right| + c$ nên ta chọn $u(x) = \frac{x}{{x + 1}}$, từ đó ta có lời giải.

Lời giải: Ta có $\left[ {\frac{x}{{x + 1}}.f(x)} \right]’$ $= \frac{1}{{{{(x + 1)}^2}}}f(x) + \frac{x}{{x + 1}}f'(x)$ $= \frac{1}{{{{(x + 1)}^2}}}.\left[ {f(x) + x(x + 1)f'(x)} \right].$

$\Rightarrow \left[ {\frac{x}{{x + 1}}.f(x)} \right]’ = \frac{1}{{{{(x + 1)}^2}}}.\left[ {{x^2} + x} \right]$ $\Leftrightarrow \left[ {\frac{x}{{x + 1}}.f(x)} \right]’ = \frac{x}{{x + 1}}$ $\Rightarrow \frac{x}{{x + 1}}.f(x) = \int {\frac{x}{{x + 1}}} dx.$

$\Rightarrow \frac{x}{{x + 1}}.f(x)$ $= \int {\left( {1 – \frac{1}{{x + 1}}} \right)} dx$ $\Rightarrow \frac{x}{{x + 1}}.f(x)$ $= x – \ln |x + 1| + c.$

Do $f(1) = – 2\ln 2$ $\Leftrightarrow \frac{1}{2}( – 2\ln 2) = 1 – \ln 2 + c$ $\Leftrightarrow c = – 1.$

$\Rightarrow \frac{x}{{x + 1}}.f(x) = x – \ln |x + 1| – 1$ $\Leftrightarrow f(x) = \frac{{{x^2} – 1 – (x + 1)\ln |x + 1|}}{x}.$

Khi đó: $I = \int_1^2 x f(x)dx$ $= \int_1^2 {\left( {{x^2} – 1 – (x + 1)\ln (x + 1)} \right)} dx$ $= \left. {\left( {\frac{{{x^3}}}{3} – x} \right)} \right|_1^2$ $– \int_1^2 {(x + 1)} \ln (x + 1)dx$ $= \frac{4}{3} – {I_1}.$

Với ${I_1} = \int_1^2 {(x + 1)} \ln (x + 1)dx.$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \ln (x + 1)}\\
{dv = (x + 1)dx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = \frac{1}{{x + 1}}dx}\\
{v = \frac{{{x^2}}}{2} + x + \frac{1}{2} = \frac{1}{2}{{(x + 1)}^2}}
\end{array}} \right..
$$

$\Rightarrow {I_1} = \left. {\left[ {\frac{1}{2}{{(x + 1)}^2}\ln (x + 1)} \right]} \right|_1^2$ $– \frac{1}{2}\int_1^2 {(x + 1)} dx$ $\Rightarrow {I_1} = \frac{9}{2}\ln 3 – 2\ln 2 – \left. {\frac{1}{2}\left( {\frac{{{x^2}}}{2} + x} \right)} \right|_1^2$ $= \frac{9}{2}\ln 3 – 2\ln 2 – \frac{5}{4}.$

Khi đó $I = \frac{4}{3} – {I_1}$ $= \frac{4}{3} – \left( {\frac{9}{2}\ln 3 – 2\ln 2 – \frac{5}{4}} \right)$ $= \frac{{31}}{{12}} – \frac{9}{2}\ln 3 + 2\ln 2.$

PHƯƠNG PHÁP 2. PHƯƠNG PHÁP ĐỔI BIẾN SỐ.

a. Kiến thức sử dụng

Công thức: $\int_a^b f [u(x)]u'(x)dx$ $= \int_{u(a)}^{u(b)} f (u)du.$

Chú ý: Đối với biến số lấy tích phân, ta có thể chọn bất kì một chữ số thay cho $x.$ Như vậy tích phân không phụ thuộc vào biến, tức là $\int_a^b f (x)dx$ $= \int_a^b f (u)du$ $= \int_a^b f (t)dt$ $= \ldots .$

b. Ví dụ áp dụng

<!-- chunk:10 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 1. Cho hàm số $f(x)$ liên tục trên $R$ và thỏa mãn $2018f(x) + f( – x) = {e^x}$ với mọi $x \in R.$ Tính tích phân $I = \int_{ – 1}^1 f (x)dx.$

Nhận xét: Giả thiết chứa $f(x)$ và $f(-x)$ nên ta biến đổi tạo ra hai biểu thức này bằng cách đặt $x = − t$, từ đó ta có lời giải.

Lời giải: Đặt $x = – t$ $\Rightarrow dx = – dt$, đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = – 1 \Rightarrow t = 1}\\
{x = 1 \Rightarrow t = – 1}
\end{array}} \right..
$$

Khi đó $I = – \int_1^{ – 1} f ( – t)dt$ $= \int_{ – 1}^1 f ( – t)dt$ $\Rightarrow I = \int_{ – 1}^1 f ( – x)dx.$

Vì $2018I + I$ $= 2018\int_{ – 1}^1 f (x)dx + \int_{ – 1}^1 f ( – x)dx.$

Nên $2019I = \int_{ – 1}^1 {\left[ {2018f(x) + f( – x)} \right]} dx$ $\Leftrightarrow 2019I = \int_{ – 1}^1 {{e^x}} dx$ $= \left. {{e^x}} \right|_{ – 1}^1 = e – \frac{1}{e}$ $\Leftrightarrow I = \frac{{{e^2} – 1}}{{2019e}}.$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 2. Cho hàm số $f(x)$ liên tục trên đoạn $\left[ {\frac{2}{3};1} \right]$ và thỏa mãn $2f(x) + 3f\left( {\frac{2}{{3x}}} \right) = 5x$ với mọi $x \in \left[ {\frac{2}{3};1} \right].$ Tính tích phân $I = \int_{\frac{2}{3}}^1 {\frac{{f(x)}}{x}} dx.$

Nhận xét: Giả thiết chứa $f(x)$ và $f\left( {\frac{2}{{3x}}} \right)$ nên ta biến đổi tạo ra hai biểu thức này bằng cách đặt $x = \frac{2}{{3t}}$, từ đó ta có lời giải.

Lời giải:

Đặt $x = \frac{2}{{3t}}$ $\Rightarrow dx = – \frac{2}{{3{t^2}}}dt$, đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = \frac{2}{3} \Rightarrow t = 1}\\
{x = 1 \Rightarrow t = \frac{2}{3}}
\end{array}} \right..
$$

Khi đó $I = – \frac{2}{3}\int_1^{\frac{2}{3}} {\frac{{f\left( {\frac{2}{{3t}}} \right).\frac{1}{{{t^2}}}}}{{\frac{2}{{3t}}}}} dt.$

$= \int_{\frac{2}{3}}^1 {\frac{{f\left( {\frac{2}{{3t}}} \right)}}{t}} dt$ $= \int_{\frac{2}{3}}^1 {\frac{{f\left( {\frac{2}{{3x}}} \right)}}{x}} dx.$

Ta có: $2I + 3I$ $= 2\int_{\frac{2}{3}}^1 {\frac{{f(x)}}{x}} dx$ $+ 3\int_{\frac{2}{3}}^1 {\frac{{f\left( {\frac{2}{{3x}}} \right)}}{x}} dx.$

$\Leftrightarrow 5I = \int_{\frac{2}{3}}^1 {\frac{{2f(x) + 3f\left( {\frac{2}{{3x}}} \right)}}{x}} dx$ $= \int_{\frac{2}{3}}^1 {\frac{{5x}}{x}} dx$ $= \int_{\frac{2}{3}}^1 5 dx = \frac{5}{3}$ $\Leftrightarrow I = \frac{1}{3}.$

<!-- chunk:12 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 3. Cho hàm số $f(x)$ liên tục trên đoạn $[0;2]$ và thỏa mãn $3f(x) – 4f(2 – x)$ $= – {x^2} – 12x + 16$ với mọi $x \in [0;2].$ Tính tích phân $I = \int_0^2 f (x)dx.$

Nhận xét: Giả thiết chứa $f(x)$ và $f(2 − x)$ nên ta biến đổi tạo ra hai biểu thức này bằng cách đặt $x = 2 − t$, từ đó ta có lời giải.

Lời giải: Đặt $x = 2 – t$ $\Rightarrow dx = – dt$, đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = 0 \Rightarrow t = 2}\\
{x = 2 \Rightarrow t = 0}
\end{array}} \right..
$$

Khi đó $I = – \int_2^0 f (2 – t)dt$ $= \int_0^2 f (2 – t)dt$ $\Rightarrow I = \int_0^2 f (2 – x)dx.$

Ta có $3I – 4I$ $= 3\int_0^2 f (x)dx – 4\int_0^2 f (2 – x)dx$ $= \int_0^2 {[3{\rm{ }}f(x) – 4{\rm{ }}f(2 – x)]dx}$ $\Leftrightarrow – I = \int_0^2 {\left( { – {x^2} – 12x + 16} \right)} dx.$

$\Leftrightarrow – I = \int_0^2 {\left( { – {x^2} – 12x + 16} \right)} dx$ $= \left. {\left( {\frac{{ – {x^3}}}{3} – 6{x^2} + 16x} \right)} \right|_0^2 = \frac{{16}}{3}$ $\Leftrightarrow I = – \frac{{16}}{3}.$

<!-- chunk:13 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 4. Cho hàm số $f(x)$ liên tục trên $R$ và thỏa mãn $f(x) = 4xf\left( {{x^2}} \right) + 2x + 1$ với mọi $x \in R.$ Tính tích phân $I = \int_0^1 f (x)dx.$

Nhận xét: Giả thiết chứa $f(x)$ và $f\left( {{x^2}} \right)$ nên ta biến đổi tạo ra hai biểu thức này bằng cách đặt $x = {t^2}$, từ đó ta có lời giải.

Lời giải: Đặt $x = {t^2}$ $\Rightarrow dx = 2tdt$, đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = 0 \Rightarrow t = 0}\\
{x = 1 \Rightarrow t = 1}
\end{array}} \right..
$$

Khi đó $I = \int_0^1 f \left( {{t^2}} \right)2tdt$ $\Rightarrow I = 2\int_0^1 x f\left( {{x^2}} \right)dx.$

Ta có $I – 2I$ $= \int_0^1 f (x)dx – 4\int_0^1 x f\left( {{x^2}} \right)dx.$

$= \int_0^1 {\left[ {f(x) – 4xf\left( {{x^2}} \right)} \right]} dx$ $= \int_0^1 {(2x + 1)} dx$ $= \left. {\left( {{x^2} + x} \right)} \right|_0^1 = 2$ $\Leftrightarrow – I = 2$ $\Leftrightarrow I = – 2.$

Nhận xét: Từ các ví dụ trên ta thấy nếu giả thiết cho mối liên hệ giữa $f(x)$ và $f(u(x))$ thì ta đặt $x = u(t).$

<!-- chunk:14 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 5. Cho hàm số $f(x)$ liên tục trên $R$ và thỏa mãn $f\left( {{x^3} + 2x – 2} \right) = 3x – 1$ với mọi $x \in R.$ Tính tích phân $I = \int_1^{10} f (x)dx.$

Lời giải: Đặt $x = {t^3} + 2t – 2$ $\Rightarrow dx = \left( {3{t^2} + 2t} \right)dt$, đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = 1 \Rightarrow {t^3} + 2t = 3 \Leftrightarrow t = 1}\\
{x = 10 \Rightarrow {t^3} + 2t = 12 \Leftrightarrow t = 2}
\end{array}} \right..
$$

Ta có $I = \int_1^2 f \left( {{t^3} + 2t – 2} \right)\left( {3{t^2} + 2t} \right)dt$ $= \int_1^2 {(3t – 1)} \left( {3{t^2} + 2t} \right)dt$ $= \int_1^2 {\left( {9{t^3} + 3{t^2} – 2t} \right)} dt.$

$= \left. {\left( {\frac{{9{t^4}}}{4} + {t^3} – {t^2}} \right)} \right|_1^2$ $= \frac{{151}}{4}.$

<!-- chunk:15 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 6. Cho hàm số $f(x)$ liên tục trên đoạn $[−1;5]$ và thỏa mãn ${[f(x)]^{2019}} + f(x) + 2 = x$ với mọi $x \in [ – 1;5].$ Tính tích phân $I = \int_0^4 f (x)dx.$

Lời giải: Đặt $t = f(x)$ $\Rightarrow {t^{2019}} + t + 2 = x$ $\Rightarrow dx = \left( {2019{t^{2018}} + 1} \right)dt.$

Đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = 0 \Rightarrow {t^{2019}} + t + 2 = 0 \Leftrightarrow t = – 1}\\
{x = 4 \Rightarrow {t^{2019}} + t + 2 = 4 \Leftrightarrow t = 1}
\end{array}} \right..
$$

Ta có $I = \int_{ – 1}^1 t \left( {2019{t^{2018}} + 1} \right)dt$ $= \int_{ – 1}^1 {\left( {2019{t^{2019}} + t} \right)} dt$ $= \left. {\left( {\frac{{2019}}{{2020}}{t^{2020}} + \frac{1}{2}{t^2}} \right)} \right|_{ – 1}^1 = 0.$

<!-- chunk:16 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 7. Biết mỗi số thực $t ≥ 0$ phương trình $4{x^3} + tx – 4 = 0$ có nghiệm dương duy nhất $x = x(t)$, với $x(t)$ là hàm số liên tục theo $t$ trên $[0; + \infty ).$ Tính tích phân $I = \int_0^7 {{{[x(t)]}^2}} dt.$

Lời giải: Đặt $t = \frac{{4 – 4{x^3}}}{x}$ $\Rightarrow dt = – \frac{{8{x^3} + 4}}{{{x^2}}}dx.$

Đổi cận: 
$$
\left\{ {\begin{array}{l}
{t = 0 \Rightarrow 4{x^3} – 4 = 0 \Leftrightarrow x = 1}\\
{t = 7 \Rightarrow 4{x^3} + 7x – 4 = 0 \Leftrightarrow x = \frac{1}{2}}
\end{array}} \right..
$$

Ta có $I = – \int_1^{\frac{1}{2}} {{x^2}} .\frac{{8{x^3} + 4}}{{{x^2}}}dx$ $= \int_{\frac{1}{2}}^1 {\left( {8{x^3} + 4} \right)} dx$ $= \left. {\left( {2{x^4} + 4x} \right)} \right|_{\frac{1}{2}}^1$ $= \frac{{31}}{8}.$

PHƯƠNG PHÁP 3. PHƯƠNG PHÁP TÍNH TÍCH PHÂN TỪNG PHẦN.

a. Kiến thức sử dụng

Công thức $\int_a^b u (x)v'(x)dx$ $= \left. {(u(x)v(x))} \right|_a^b$ $– \int_a^b v (x)u'(x)dx$ (trong đó $u$, $v$ có đạo hàm liên tục trên $K$ và $a$, $b$ là hai số thuộc $K$).

b. Ví dụ áp dụng

<!-- chunk:17 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 1. Cho hàm số $f(x)$ liên tục, có đạo hàm trên $R$ thỏa mãn $f(\sqrt 3 ) = \sqrt 3$ và $\int_0^{\sqrt 3 } {\frac{{f(x)dx}}{{\sqrt {1 + {x^2}} }}} = 1.$ Tính tích phân $I = \int_0^{\sqrt 3 } {f’} (x)\ln (x + \sqrt {1 + {x^2}} )dx.$

Lời giải: Đặt 
$$
\left\{ {\begin{array}{l}
{u = \ln \left( {x + \sqrt {1 + {x^2}} } \right)}\\
{dv = f'(x)dx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = \frac{1}{{\sqrt {1 + {x^2}} }}dx}\\
{v = f(x)}
\end{array}} \right..
$$

Khi đó $I = \left. {f(x)\ln \left( {x + \sqrt {1 + {x^2}} } \right)} \right|_0^{\sqrt 3 }$ $– \int_0^{\sqrt 3 } {\frac{{f(x)dx}}{{\sqrt {1 + {x^2}} }}}$ $= \sqrt 3 \ln (2 + \sqrt 3 ) – 1.$

<!-- chunk:18 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 2. Cho hàm số $f(x)$ liên tục, có đạo hàm trên $R$ thỏa mãn $2f(3) – f(0) = 18$ và $\int_0^3 {\left( {f'(x) + 1} \right)} \sqrt {x + 1} dx$ $= \frac{{302}}{{15}}.$ Tính tích phân $I = \int_0^3 {\frac{{f(x)}}{{\sqrt {x + 1} }}} dx.$

Lời giải: Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt {x + 1} }\\
{dv = \left( {f'(x) + 1} \right)dx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = \frac{1}{{2\sqrt {x + 1} }}dx}\\
{v = f(x) + x + 1}
\end{array}} \right..
$$

Khi đó $\frac{{302}}{{15}} = \left. {\left[ {(f(x) + x + 1)\sqrt {x + 1} } \right]} \right|_0^3$ $– \int_0^3 {\left[ {\frac{{f(x)}}{{2\sqrt {x + 1} }} + \frac{{\sqrt {x + 1} }}{2}} \right]} dx.$

$= 2f(3) – f(0)$ $+ 7 – \frac{I}{2} – \frac{1}{2}\int_0^3 {\sqrt {x + 1} } dx$ $\Leftrightarrow \frac{{302}}{{15}} = 25 – \frac{I}{2} – \frac{{14}}{6}$ $\Rightarrow I = \frac{{76}}{{15}}.$

<!-- chunk:19 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 3. Cho hàm số $f(x)$ liên tục, có đạo hàm trên đoạn $[1;3]$ thỏa mãn $f(3) = f(1) = 3$ và $\int_1^3 {\frac{{xf'(x)}}{{x + 1}}} dx = 0.$ Tính tích phân $I = \int_1^3 {\frac{{f(x) + \ln x}}{{{{(x + 1)}^2}}}} dx.$

Lời giải: Xét $I = \int_1^3 {\frac{{f(x) + \ln x}}{{{{(x + 1)}^2}}}} dx$, đặt 
$$
\left\{ {\begin{array}{l}
{u = f(x) + \ln x}\\
{dv = \frac{1}{{{{(x + 1)}^2}}}dx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = \left( {f'(x) + \frac{1}{x}} \right)dx}\\
{v = – \frac{1}{{x + 1}} + 1 = \frac{x}{{x + 1}}}
\end{array}} \right..
$$

Khi đó $I = \left. {\left[ {\frac{x}{{x + 1}}(f(x) + \ln x)} \right]} \right|_1^3$ $– \int_1^3 {\left[ {\frac{{xf'(x)}}{{x + 1}} + \frac{1}{{x + 1}}} \right]} dx.$

${ = \frac{3}{4}(f(3) + \ln 3)}$ ${ – \frac{1}{2}f(1)}$ $– \left[ {0 + \left. {\ln |x + 1|} \right|_1^3} \right]$ $= \frac{3}{4} + \frac{3}{4}\ln 3 – \ln 2.$

<!-- chunk:20 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 4. Cho hàm số $f(x)$ liên tục, có đạo hàm trên đoạn $[0;1]$ thỏa mãn $f(1) = \frac{1}{2}$ và $\int_0^1 {\left( {f'(x) + x} \right)} \ln \left( {1 + {x^2}} \right)dx$ $= 2\ln 2 – 1.$ Tính tích phân $I = \int_0^1 {\frac{{xf(x)}}{{1 + {x^2}}}} dx.$

Lời giải: Xét $\int_0^1 {\left( {f'(x) + x} \right)} \ln \left( {1 + {x^2}} \right)dx$ $= 2\ln 2 – 1$, đặt 
$$
\left\{ {\begin{array}{l}
{u = \ln \left( {1 + {x^2}} \right)}\\
{dv = \left( {f'(x) + x} \right)dx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = \frac{{2x}}{{1 + {x^2}}}dx}\\
{v = f(x) + \frac{{{x^2}}}{2} + \frac{1}{2}}
\end{array}} \right..
$$

Khi đó $2\ln 2 – 1$ $= \left. {\left[ {\left( {f(x) + \frac{{{x^2} + 1}}{2}} \right)\ln \left( {1 + {x^2}} \right)} \right]} \right|_0^1$ $– \int_0^1 {\left( {\frac{{2xf(x)}}{{1 + {x^2}}} + x} \right)} dx.$

$= (f(1) + 1)\ln 2$ $– 2\int_0^1 {\frac{{xf(x)}}{{1 + {x^2}}}} dx$ $– \int_0^1 x dx$ $\Leftrightarrow 2\ln 2 – 1$ $= \frac{3}{2}\ln 2 – 2I – \frac{1}{2}$ $\Leftrightarrow I = \frac{1}{4} – \frac{1}{4}\ln 2.$

PHƯƠNG PHÁP 4. TẠO BÌNH PHƯƠNG CHO HÀM SỐ DƯỚI DẤU TÍCH PHÂN.
a. Kiến thức sử dụng
Nếu $f(x) \ge 0$ với mọi $x \in [a;b]$ thì $\int_a^b f (x)dx \ge 0$, dấu bằng xảy ra $\Leftrightarrow f(x) = 0$, $\forall x \in [a;b].$

Hệ quả: $\int_a^b {{f^2}} (x)dx = 0$ $\Leftrightarrow f(x) = 0$ với mọi $x \in [a;b].$

b. Ví dụ áp dụng

<!-- chunk:21 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 1. Cho hàm số $f(x)$ liên tục, có đạo hàm trên đoạn $[0;1].$ Biết $\int_0^1 x f(x)dx = 1$ và $\int_0^1 {{{[f(x)]}^2}dx} = 3.$ Tính tích phân $I = \int_0^1 {{{[f(x)]}^{2018}}dx} .$

Nhận xét: Giả thiết chứa ${[f(x)]^2}$ và $xf(x)$ nên ta tạo bình phương dạng ${[f(x) – ax]^2}.$ Ta chọn $a$ sao cho $\int_0^1 {{{[f(x) – ax]}^2}dx} = 0$ $\Leftrightarrow \int_0^1 {\left( {{{[f(x)]}^2} – 2axf(x) + {a^2}{x^2}} \right)} dx = 0$ $\Leftrightarrow \int_0^1 {{{[f(x)]}^2}dx}$ $– 2a\int_0^1 x f(x)dx$ $+ {a^2}\int_0^1 {{x^2}} dx = 0$ $\Leftrightarrow 3 – 2a + \frac{{{a^2}}}{3} = 0$ $\Leftrightarrow a = 3.$ Từ đó ta có lời giải.

Lời giải: Ta có $\int_0^1 {{{[f(x) – 3x]}^2}dx} = 0$ $\Leftrightarrow \int_0^1 {\left( {{{[f(x)]}^2} – 6xf(x) + 9{x^2}} \right)} dx$ $= \int_0^1 {{{[f(x)]}^2}dx}$ $– 6\int_0^1 x f(x)dx$ $+ 9\int_0^1 {{x^2}} dx.$

$\Leftrightarrow 3 – 6 + 3 = 0$ $\Rightarrow f(x) = 3x.$

Khi đó $I = \int_0^1 {{{[f(x)]}^{2018}}dx}$ $= {3^{2018}}\int_0^1 {{x^{2018}}} dx$ $= \frac{{{3^{2018}}}}{{2019}}.$

<!-- chunk:22 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 2. Cho hàm số $f(x)$ liên tục, có đạo hàm trên đoạn $\left[ {0;\frac{\pi }{2}} \right].$ Biết $f\left( {\frac{\pi }{2}} \right) = 0$, $\int_0^{\frac{\pi }{2}} {{{\left[ {f'(x)} \right]}^2}} dx = \pi$ và $\int_0^{\frac{\pi }{2}} {\cos x.f(x)dx} = \frac{\pi }{2}.$ Tính tích phân $I = \int_0^{\frac{\pi }{2}} f (x)dx.$

Nhận xét: Giả thiết chứa ${\left[ {f'(x)} \right]^2}$ và $f(x)$ nên ta chưa thể tạo bình phương, do đó trước hết ta biến đổi $\int_0^{\frac{\pi }{2}} {\cos x.f(x)dx}$ để tạo biểu thức $f'(x)$ bằng cách đặt:

$$
\left\{ {\begin{array}{l}
{u = f(x)}\\
{dv = \cos xdx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = f'(x)dx}\\
{v = \sin x}
\end{array}} \right.
$$
, khi đó $\frac{\pi }{2} = \left. {(f(x)\sin x)} \right|_0^{\frac{\pi }{2}} – \int_0^{\frac{\pi }{2}} {f'(x)\sin xdx} .$

$\Rightarrow \int_0^{\frac{\pi }{2}} {f'(x)\sin xdx} = – \frac{\pi }{2}.$

Đến đây ta được hai biểu thức ${\left[ {f'(x)} \right]^2}$ và $f'(x).\sin x$ nên ta tạo bình phương dạng ${\left[ {f'(x) – a\sin x} \right]^2}.$

Ta chọn $a$ sao cho $\int_0^{\frac{\pi }{2}} {{{\left[ {f'(x) – a\sin x} \right]}^2}} dx = 0$ $\Leftrightarrow \int_0^{\frac{\pi }{2}} {\left( {{{\left[ {f'(x)} \right]}^2} – 2a\sin x.f'(x) + {a^2}{{\sin }^2}x} \right)dx} = 0.$

$\Leftrightarrow \int_0^{\frac{\pi }{2}} {{{\left[ {f'(x)} \right]}^2}} dx$ $– 2a\int_0^{\frac{\pi }{2}} {\sin x.f'(x)dx}$ $+ {a^2}\int_0^{\frac{\pi }{2}} {{{\sin }^2}xdx} = 0$ $\Leftrightarrow \pi + a\pi + \frac{{\pi {a^2}}}{4} = 0$ $\Leftrightarrow \pi {\left( {\frac{a}{2} + 1} \right)^2} = 0$ $\Leftrightarrow a = – 2.$ Từ đó ta có lời giải.

Lời giải: Xét $\int_0^{\frac{\pi }{2}} {\cos x.f(x)dx} = \frac{\pi }{2}$, đặt 
$$
\left\{ {\begin{array}{l}
{u = f(x)}\\
{dv = \cos xdx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = f'(x)dx}\\
{v = \sin x}
\end{array}} \right..
$$

Khi đó $\frac{\pi }{2} = \left. {(f(x)\sin x)} \right|_0^{\frac{\pi }{2}}$ $– \int_0^{\frac{\pi }{2}} {f'(x)\sin xdx}$ $\Rightarrow \int_0^{\frac{\pi }{2}} {f'(x)\sin xdx}$ $= – \frac{\pi }{2}.$

Ta có: $\int_0^{\frac{\pi }{2}} {{{\left[ {f'(x) + 2\sin x} \right]}^2}} dx = 0$ $\Leftrightarrow \int_0^{\frac{\pi }{2}} {\left( {{{\left[ {f'(x)} \right]}^2} + 4\sin x.f'(x) + 4{{\sin }^2}x} \right)dx}$ $= \pi – 2\pi + \frac{{4\pi }}{4} = 0$ $\Rightarrow f'(x) = – 2\sin x.$

$\Rightarrow f(x) = 2\cos x + c$ mà $f\left( {\frac{\pi }{2}} \right) = 0$ $\Rightarrow c = 0$ nên ta có $f(x) = 2\cos x.$

Ta có $I = \int_0^{\frac{\pi }{2}} f (x)dx$ $= 2\int_0^{\frac{\pi }{2}} {\cos xdx} = 2.$

<!-- chunk:23 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 3. Cho hàm số $f(x)$ liên tục, có đạo hàm trên đoạn $[−1;0 ].$ Biết $f( – 1) = – \frac{7}{{10}}$, $\int_{ – 1}^0 {{{\left[ {\frac{{f'(x)}}{x}} \right]}^2}} dx = \frac{{169}}{{105}}$ và $\int_{ – 1}^0 {(x – 1)} .f(x)dx = \frac{{103}}{{420}}.$ Tính tích phân $I = \int_0^1 f (x)dx.$

Nhận xét: Giả thiết chứa ${\left[ {\frac{{f'(x)}}{x}} \right]^2}$ và $f(x)$ nên ta chưa thể tạo bình phương, do đó trước hết ta biến đổi $\int_{ – 1}^0 {(x – 1)} .f(x)dx$ để đưa về $f'(x)$ bằng cách đặt:

$$
\left\{ {\begin{array}{l}
{u = f(x)}\\
{dv = (x – 1)dx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = f'(x)dx}\\
{v = \frac{{{x^2}}}{2} – x}
\end{array}} \right.
$$
, khi đó $\frac{{103}}{{420}} = \left. {\left[ {\left( {\frac{{{x^2}}}{2} – x} \right)f(x)} \right]} \right|_{ – 1}^0$ $– \frac{1}{2}\int_{ – 1}^0 {\left( {{x^2} – 2x} \right)} f'(x)dx.$

$\Rightarrow \int_{ – 1}^0 {\left( {{x^2} – 2x} \right)} f'(x)dx = \frac{{169}}{{105}}.$

Đến đây ta được hai biểu thức ${\left[ {\frac{{f'(x)}}{x}} \right]^2}$ và $\left( {{x^2} – 2x} \right)f'(x)$ nên ta tạo bình phương dạng ${\left[ {\frac{{f'(x)}}{x} – a\left( {{x^3} – 2{x^2}} \right)} \right]^2}$, ta chọn $a$ sao cho:

$\int_0^1 {{{\left[ {\frac{{f'(x)}}{x} – a\left( {{x^3} – 2{x^2}} \right)} \right]}^2}} dx = 0$ $\Leftrightarrow \int_0^1 {\left( {{{\left[ {\frac{{f'(x)}}{x}} \right]}^2} – 2a\left( {{x^3} – 2{x^2}} \right).\frac{{f'(x)}}{x} + {a^2}{{\left( {{x^3} – 2{x^2}} \right)}^2}} \right)dx} = 0.$

$\Leftrightarrow \int_0^1 {{{\left[ {\frac{{f'(x)}}{x}} \right]}^2}} dx$ $– 2a\int_0^1 {\left( {{x^2} – 2x} \right)} .f'(x)dx$ $+ {a^2}\int_0^1 {{{\left( {{x^3} – 2{x^2}} \right)}^2}} dx = 0.$

$\Leftrightarrow \frac{{169}}{{105}} – 2a.\frac{{169}}{{105}} + \frac{{169}}{{105}}{a^2} = 0$ $\Leftrightarrow a = 1.$ Từ đó ta có lời giải.

Lời giải:

Xét $\int_{ – 1}^0 {(x – 1)} .f(x)dx = \frac{{103}}{{420}}$, đặt 
$$
\left\{ {\begin{array}{l}
{u = f(x)}\\
{dv = (x – 1)dx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = f'(x)dx}\\
{v = \frac{{{x^2}}}{2} – x}
\end{array}} \right.
$$
, khi đó:

$\frac{{103}}{{420}} = \left. {\left[ {\left( {\frac{{{x^2}}}{2} – x} \right)f(x)} \right]} \right|_{ – 1}^0$ $– \frac{1}{2}\int_{ – 1}^0 {\left( {{x^2} – 2x} \right)} f'(x)dx$ $\Rightarrow \int_{ – 1}^0 {\left( {{x^2} – 2x} \right)} f'(x)dx = \frac{{169}}{{105}}.$

Ta có $\int_0^1 {{{\left[ {\frac{{f'(x)}}{x} – \left( {{x^3} – 2{x^2}} \right)} \right]}^2}} dx = 0$ $\Leftrightarrow \int_0^1 {\left( {{{\left[ {\frac{{f'(x)}}{x}} \right]}^2} – 2\left( {{x^3} – 2{x^2}} \right).\frac{{f'(x)}}{x} + {{\left( {{x^3} – 2{x^2}} \right)}^2}} \right)} dx.$

$= \int_0^1 {{{\left[ {\frac{{f'(x)}}{x}} \right]}^2}} dx$ $– 2\int_0^1 {\left( {{x^2} – 2x} \right)} .f'(x)dx$ $+ \int_0^1 {{{\left( {{x^3} – 2{x^2}} \right)}^2}} dx$ $= \frac{{169}}{{105}} – 2.\frac{{169}}{{105}} + \frac{{169}}{{105}} = 0.$

$\Rightarrow \frac{{f'(x)}}{x} = {x^3} – 2{x^2}$ $\Leftrightarrow f'(x) = {x^4} – 2{x^3}$ $\Rightarrow f(x) = \frac{1}{5}{x^5} – \frac{1}{2}{x^4} + c.$

Mà $f( – 1) = – \frac{7}{{10}}$ $\Rightarrow c = 0.$

Nên $f(x) = \frac{1}{5}{x^5} – \frac{1}{2}{x^4}.$

Khi đó $I = \int_0^1 f (x)dx$ $= \int_0^1 {\left( {\frac{1}{5}{x^5} – \frac{1}{2}{x^4}} \right)dx}$ $= \left. {\left( {\frac{1}{{30}}{x^6} – \frac{1}{{10}}{x^5}} \right)} \right|_0^1$ $= – \frac{1}{{15}}.$

<!-- chunk:24 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 4. Cho hàm số $f(x)$ liên tục, có đạo hàm trên đoạn $[0;2].$ Biết $f(2) = 7$ và ${\left[ {f'(x)} \right]^2} = 21{x^4} – 12x – 12xf(x)$ với mọi $x \in [0;2].$ Tính tích phân $I = \int_0^2 f (x)dx.$

Lời giải: Từ giả thiết ta có $\int_0^2 {{{\left[ {f'(x)} \right]}^2}} dx$ $= \int_0^2 {\left[ {21{x^4} – 12x – 12xf(x)} \right]dx} .$

$\Rightarrow \int_0^2 {{{\left[ {f'(x)} \right]}^2}} dx$ $= \int_0^2 {\left( {21{x^4} – 12x} \right)dx}$ $– 12\int_0^2 x f(x)dx$ $\Rightarrow \int_0^2 {{{\left[ {f'(x)} \right]}^2}} dx$ $= \frac{{552}}{5} – 12\int_0^2 x f(x)dx$ $(*).$

Đến đây ta có hai biểu thức ${\left[ {f'(x)} \right]^2}$ và $f(x)$ nên ta chưa thể tạo bình phương, do đó trước hết ta biến đổi $\int_0^2 x f(x)dx$ để tạo ra $f'(x)$ bằng cách đặt 
$$
\left\{ {\begin{array}{l}
{u = f(x)}\\
{dv = xdx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = f'(x)dx}\\
{v = \frac{{{x^2}}}{2}}
\end{array}} \right..
$$

Khi đó $\int_0^2 x f(x)dx$ $= \left. {\left[ {\frac{{{x^2}}}{2}f(x)} \right]} \right|_0^2$ $– \frac{1}{2}\int_0^2 {{x^2}} f'(x)dx$ $= 14 – \frac{1}{2}\int_0^2 {{x^2}} f'(x)dx$, thế vào $(*)$ ta được:

$\int_0^2 {{{\left[ {f'(x)} \right]}^2}} dx$ $= \frac{{552}}{5}$ $– 12\left[ {14 – \frac{1}{2}\int_0^2 {{x^2}} f'(x)dx} \right]$ $\Leftrightarrow \int_0^2 {{{\left[ {f'(x)} \right]}^2}} dx$ $– 6\int_0^2 {{x^2}} f'(x)dx$ $+ \frac{{288}}{5}$ $= 0$ $(**).$

Mà $\int_0^2 9 {x^4}dx = \frac{{288}}{5}$ nên ta có $(**)$ $\Leftrightarrow \int_0^2 {{{\left[ {f'(x)} \right]}^2}} dx$ $– 6\int_0^2 {{x^2}} f'(x)dx$ $+ \int_0^2 9 {x^4}dx = 0.$

$\Leftrightarrow \int_0^2 {{{\left[ {f'(x) – 3{x^2}} \right]}^2}} dx = 0$ $\Rightarrow f'(x) = 3{x^2}$ $\Rightarrow f(x) = {x^3} + c$ mà $f(2) = 7$ $\Rightarrow c = – 1$ $\Rightarrow f(x) = {x^3} – 1.$

Khi đó $I = \int_0^2 f (x)dx$ $= \int_0^2 {\left( {{x^3} – 1} \right)dx} = 2.$

<!-- chunk:25 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 5. Cho hàm số $f(x)$ liên tục trên đoạn $[0;1]$ thỏa mãn $\int_0^1 f (x)dx = 2.$ Biết $\int_0^1 x f(x)dx = \frac{7}{6}$ và $\int_0^1 {{{[f(x)]}^2}dx} = \frac{{13}}{3}.$ Tính tích phân $I = \int_0^1 {{{[f(x)]}^3}dx} .$

Nhận xét: Giả thiết chứa ${[f(x)]^2}$, $xf(x)$ và $f(x)$ nên ta tạo bình phương dạng ${[f(x) + ax + b]^2}.$ Ta chọn $a$, $b$ sao cho $\int_0^1 {{{[f(x) + ax + b]}^2}dx} = 0.$

$\Leftrightarrow \int_0^1 {\left( {{{[f(x)]}^2} + 2axf(x) + 2bf(x) + 2abx + {a^2}{x^2} + {b^2}} \right)dx} = 0.$

$\Leftrightarrow \int_0^1 {{{[f(x)]}^2}dx}$ $+ 2a\int_0^1 x f(x)dx$ $+ 2b\int_0^1 f (x)dx$ $+ 2ab\int_0^1 x dx$ $+ \int_0^1 {\left( {{a^2}{x^2} + {b^2}} \right)dx} = 0.$

$\Leftrightarrow \frac{{13}}{3} + 2a.\frac{7}{6} + 4b + ab + \frac{{{a^2}}}{3} + {b^2} = 0$ $\Leftrightarrow {a^2} + (3b + 7)a + 3{b^2} + 12b + 13 = 0.$

Để có $a$ thì $\Delta = {(3b + 7)^2} – 4\left( {3{b^2} + 12b + 13} \right) \ge 0$ $\Leftrightarrow – 3{(b + 1)^2} \ge 0$ $\Leftrightarrow b = – 1$ $\Rightarrow a = – 2$, từ đó ta có lời giải.

Lời giải: Ta có $\int_0^1 {{{[f(x) – 2x – 1]}^2}dx}$ $= \int_0^1 {\left( {{{[f(x)]}^2} – 4xf(x) – 2f(x) + 4x + 4{x^2} + 1} \right)dx} .$

$= \int_0^1 {{{[f(x)]}^2}dx}$ $– 4\int_0^1 x f(x)dx$ $– 2\int_0^1 f (x)dx$ $+ 4\int_0^1 {xdx}$ $+ \int_0^1 {\left( {4{x^2} + 1} \right)dx} = 0.$

$= \frac{{13}}{3} – 4.\frac{7}{6} – 4 + 2 + \frac{4}{3} + 1 = 0$ $\Rightarrow f(x) = 2x + 1.$

Khi đó $I = \int_0^1 {{{[f(x)]}^3}dx}$ $= \int_0^1 {{{(2x + 1)}^3}} dx = 10.$

<!-- chunk:26 level:3 source:https://toanmath.com/2019/12/mot-so-phuong-phap-tinh-tich-phan-ham-an.html -->
## Ví dụ 6. Cho hàm số $f(x)$ liên tục trên đoạn $\left[ {0;\frac{\pi }{2}} \right]$ thỏa mãn $\int_0^{\frac{\pi }{2}} f (x)dx = \frac{\pi }{2} + 1$, $\int_0^{\frac{\pi }{2}} {\sin x.f(x)dx}$ $= \frac{\pi }{4} + 1$ và $\int_0^{\frac{\pi }{2}} {{{[f(x)]}^2}dx} = \frac{{3\pi }}{4} + 2.$ Tính tích phân $I = \int_0^{\frac{\pi }{2}} f (x).\cos xdx.$

Nhận xét: Giả thiết chứa ${[f(x)]^2}$, $\sin x.f(x)$ và $f(x)$ nên ta tạo bình phương dạng ${[f(x) + a\sin x + b]^2}$, ta chọn $a$, $b$ sao cho $\int_0^{\frac{\pi }{2}} {{{[f(x) + a\sin x + b]}^2}dx} = 0.$

$\Leftrightarrow \int_0^{\frac{\pi }{2}} {\left( {{{[f(x)]}^2} + 2a\sin xf(x) + 2bf(x) + 2ab\sin x + {a^2}{{\sin }^2}x + {b^2}} \right)dx} = 0.$

$\Leftrightarrow \int_0^{\frac{\pi }{2}} {{{[f(x)]}^2}dx}$ $+ 2a\int_0^{\frac{\pi }{2}} {\sin xf(x)dx}$ $+ 2b\int_0^{\frac{\pi }{2}} f (x)dx$ $+ 2ab\int_0^{\frac{\pi }{2}} {\sin xdx}$ $+ \int_0^{\frac{\pi }{2}} {\left( {{a^2}{{\sin }^2}x + {b^2}} \right)dx} = 0.$

$\Leftrightarrow \frac{{3\pi }}{4} + 2$ $+ 2a\left( {\frac{\pi }{4} + 1} \right)$ $+ 2b\left( {\frac{\pi }{2} + 1} \right)$ $+ 2ab + \frac{{\pi {a^2}}}{4}$ $+ \frac{{\pi {b^2}}}{2} = 0.$

$\Leftrightarrow \pi {(a + 1)^2}$ $+ 8(a + 1)(b + 1)$ $+ 2\pi {(b + 1)^2} = 0.$

Để có $a$ thì $\Delta ‘ = 16{(b + 1)^2} – 2{\pi ^2}{(b + 1)^2} \ge 0$ $\Leftrightarrow \left( {16 – 2{\pi ^2}} \right){(b + 1)^2} \ge 0$ $\Leftrightarrow b = – 1$ $\Rightarrow a = – 1.$ Từ đó ta có lời giải.

Lời giải: Ta có $\int_0^{\frac{\pi }{2}} {{{[f(x) – \sin x – 1]}^2}dx}$ $= \int_0^{\frac{\pi }{2}} {\left( {{{[f(x)]}^2} – 2\sin xf(x) – 2f(x) + 2\sin x + {{\sin }^2}x + 1} \right)dx} = 0.$

$\Leftrightarrow \int_0^{\frac{\pi }{2}} {{{[f(x)]}^2}dx}$ $– 2\int_0^{\frac{\pi }{2}} {\sin xf(x)dx}$ $– 2\int_0^{\frac{\pi }{2}} f (x)dx$ $+ 2\int_0^{\frac{\pi }{2}} {\sin xdx}$ $+ \int_0^{\frac{\pi }{2}} {\left( {{{\sin }^2}x + 1} \right)dx.}$

$= \frac{{3\pi }}{4} + 2$ $– 2\left( {\frac{\pi }{4} + 1} \right)$ $– 2\left( {\frac{\pi }{2} + 1} \right)$ $+ 2 + \frac{{3\pi }}{4} = 0$ $\Rightarrow f(x) = \sin x + 1.$

Ta có: $I = \int_0^{\frac{\pi }{2}} {(\sin x + 1)} \cos xdx = \frac{3}{2}.$