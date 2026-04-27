# Cách giải phương trình bậc 3 tổng quát

<!-- chunk:0 level:0 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-3-tong-quat.html -->
Bài viết hướng dẫn một số cách giải phương trình bậc 3 tổng quát: phân tích nhân tử, phương pháp Cardano, phương pháp lượng giác hóa – hàm hyperbolic. Tùy vào các phương trình bậc 3 (phương trình bậc ba) sẽ có các cách giải phù hợp để thu được lời ngắn gọn, dễ hiểu.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-3-tong-quat.html -->
## A. CÁCH GIẢI PHƯƠNG TRÌNH BẬC 3 TỔNG QUÁT
1. Phương pháp phân tích nhân tử
Nếu phương trình bậc ba $a{x^3} + b{x^2} + cx + d = 0$ có nghiệm $x = r$ thì có nhân tử $(x – r)$, do đó có thể phân tích: $a{x^3} + b{x^2} + cx + d$ $= \left( {x – r} \right)\left[ {a{x^2} + \left( {b + ar} \right)x + c + br + a{r^2}} \right].$

Từ đó ta đưa về giải một phương trình bậc hai, có nghiệm là: $\frac{{ – b – ra \pm \sqrt {{b^2} – 4ac – 2abr – 3{a^2}{r^2}} }}{{2a}}.$

2. Phương pháp Cardano
Xét phương trình bậc ba ${x^3} + a{x^2} + bx + c = 0$ $(1).$

Đặt $x = y – \frac{a}{3}$, phương trình $(1)$ luôn biến đổi được về dạng chính tắc: ${y^3} + py + q = 0$ $(2)$, trong đó: $p = b – \frac{{{a^2}}}{3}$, $q = c + \frac{{2{a^3} – 9ab}}{{27}}.$

Ta chỉ xét $p,q \ne 0$ vì nếu $p=0$ hoặc $q=0$ thì đưa về trường hợp đơn giản.

Đặt $y=u+v$ thay vào phương trình $(2)$, ta được: ${\left( {u + v} \right)^3} + p\left( {u + v} \right) + q = 0$ $\Leftrightarrow {u^3} + {v^3} + \left( {3uv + p} \right)\left( {u + v} \right) + q = 0$ $(3).$

Chọn $u$, $v$ sao cho $3uv+p=0$ $(4).$

Như vậy, để tìm $u$ và $v$, từ $(3)$ và $(4)$ ta có hệ phương trình: 
$$
\left\{ \begin{array}{l}
{u^3} + {v^3} = – q\\
{u^3}{v^3} = – \frac{{{p^3}}}{{27}}
\end{array} \right.
$$

Theo định lí Vi-ét, ${u^3}$ và ${v^3}$ là hai nghiệm của phương trình: ${X^2} + qX – \frac{{{p^3}}}{{27}} = 0$ $(5).$

Đặt $\Delta = \frac{{{q^2}}}{4} + \frac{{{p^3}}}{{27}}.$

• Khi $Δ > 0$, phương trình $(5)$ có nghiệm: ${u^3} = – \frac{q}{2} + \sqrt \Delta$, ${v^3} = – \frac{q}{2} – \sqrt \Delta .$

Như vậy phương trình $(2)$ sẽ có nghiệm thực duy nhất là: $y = \sqrt[3]{{ – \frac{q}{2} + \sqrt \Delta }} + \sqrt[3]{{ – \frac{q}{2} – \sqrt \Delta }}.$

• Khi $Δ=0$, phương trình $(5)$ có nghiệm kép: $u = v = – \sqrt[3]{{\frac{q}{2}}}.$

Khi đó, phương trình $(2)$ có hai nghiệm thực, trong đó một nghiệm kép: ${y_1} = 2\sqrt[3]{{ – \frac{q}{2}}}$, ${y_2} = {y_3} = \sqrt[3]{{\frac{q}{2}}}.$

• Khi $Δ < 0$, phương trình $(5)$ có nghiệm phức.

Gọi $u_0^3$ là một nghiệm phức của $(5)$, $v_0^3$ là giá trị tương ứng sao cho ${u_0}{v_0} = – \frac{p}{3}.$

Khi đó, phương trình $(2)$ có ba nghiệm phân biệt: ${y_1} = {u_0} + {v_0}$, ${y_2} = – \frac{1}{2}\left( {{u_0} + {v_0}} \right) + i\frac{{\sqrt 3 }}{2}\left( {{u_0} – {v_0}} \right)$, ${y_3} = – \frac{1}{2}\left( {{u_0} + {v_0}} \right) – i\frac{{\sqrt 3 }}{2}\left( {{u_0} – {v_0}} \right).$

3. Phương pháp lượng giác hoá
Một phương trình bậc ba, nếu có $3$ nghiệm thực, khi biểu diễn dưới dạng căn thức sẽ liên quan đến số phức. Vì vậy ta thường dùng phương pháp lượng giác hoá để tìm một cách biểu diễn khác đơn giản hơn, dựa trên hai hàm số $\cos$ và $\arccos.$

Cụ thể, từ phương trình ${t^3} + pt + q = 0$ $(*)$, ta đặt $t = u\cos \alpha$ và tìm $u$ để có thể đưa  $(*)$ về dạng: $4{\cos ^3}\alpha – 3\cos \alpha – cos3\alpha = 0.$

Muốn vậy, ta chọn $u = 2\sqrt {\frac{{ – p}}{3}}$ và chia $2$ vế của $(*)$ cho $\frac{{{u^3}}}{4}$ để được: $4{\cos ^3}\alpha – 3\cos \alpha – \frac{{3q}}{{2p}}\sqrt {\frac{{ – 3}}{p}} = 0$ $\Leftrightarrow \cos 3\alpha = \frac{{3q}}{{2p}}\sqrt {\frac{{ – 3}}{p}} .$

Vậy $3$ nghiệm thực là: ${t_i} = 2\sqrt {\frac{{ – p}}{3}} \cos \left[ {\frac{1}{3}\arccos \left( {\frac{{3q}}{{2p}}\sqrt {\frac{{ – 3}}{p}} } \right) – \frac{{2i\pi }}{3}} \right]$ với $i = 0, 1, 2.$

Lưu ý rằng nếu phương trình có $3$ nghiệm thực thì $p < 0$ (điều ngược lại không đúng) nên công thức trên không có số phức.

[ads]

<!-- chunk:2 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-3-tong-quat.html -->
## Ví dụ 1. Giải phương trình: ${x^3} + {x^2} + x = – \frac{1}{3}.$

Phương trình không có nghiệm hữu tỉ nên không thể phân tích nhân tử. Trước khi nghĩ tới công thức Cardano, ta thử quy đồng phương trình: $3{x^3} + 3{x^2} + 3x + 1 = 0.$

Đại lượng $3{x^2} + 3x + 1$ gợi ta đến hằng đẳng thức quen thuộc sau: ${x^3} + 3{x^2} + 3x + 1 = {\left( {x + 1} \right)^3}.$

Do đó phương trình tương đương: ${\left( {x + 1} \right)^3} = – 2{x^3}$ $\Leftrightarrow x + 1 = – \sqrt[3]{2}x.$

Từ đó suy ra phương trình có nghiệm duy nhất: $x = \frac{{ – 1}}{{1 + \sqrt[3]{2}}}.$

Nhận xét: Ví dụ trên là một phương trình bậc ba có nghiệm vô tỉ và được giải nhờ khéo léo biến đổi đẳng thức. Tuy nhiên, những bài đơn giản như thế này không có nhiều. Sau đây ta sẽ đi sâu vào công thức Cardano:

<!-- chunk:3 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-3-tong-quat.html -->
## Ví dụ 2. Giải phương trình: ${x^3} – 3{x^2} + 4x + 11 = 0.$

Đặt $x = y + 1$, thế vào phương trình đầu bài, ta được: ${y^3} + 1.y + 13 = 0.$

Tính $\Delta = {13^2} + \frac{4}{{27}}{.1^3}$ $= \frac{{4567}}{{27}} \ge 0.$

Áp dụng công thức Cardano suy ra: $y = \sqrt[3]{{\frac{{ – 13 + \sqrt {\frac{{4567}}{{27}}} }}{2}}}$ $+ \sqrt[3]{{\frac{{ – 13 – \sqrt {\frac{{4567}}{{27}}} }}{2}}}.$

Suy ra: $x = \sqrt[3]{{\frac{{ – 13 + \sqrt {\frac{{4567}}{{27}}} }}{2}}}$ $+ \sqrt[3]{{\frac{{ – 13 – \sqrt {\frac{{4567}}{{27}}} }}{2}}} + 1.$

Nhận xét: Ví dụ trên là một ứng dụng cơ bản của công thức Cardano. Tuy nhiên, công thức này không hề dễ nhớ và chỉ được dùng trong các kì thi học sinh giỏi. Vì thế, có lẽ chúng ta sẽ cố gắng tìm một con đường “hợp thức hóa” các lời giải trên, đó là phương pháp lượng giác hoá. Đầu tiên xét phương trình dạng $x^3 + px + q = 0$ với $p <0$ và có $1$ nghiệm thực:

<!-- chunk:4 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-3-tong-quat.html -->
## Ví dụ 3. Giải phương trình: ${x^3} + 3{x^2} + 2x – 1 = 0.$

Đầu tiên đặt $x=y-1$ ta đưa về phương trình ${y^3} – y – 1 = 0$ $(1)$, đến đây ta dùng lượng giác như sau:

Nếu $\left| y \right| < \frac{2}{{\sqrt 3 }}$, suy ra $\left| {\frac{{\sqrt 3 }}{2}y} \right| < 1$, do đó tồn tại $\alpha \in \left[ {0,\pi } \right]$ sao cho $\frac{{\sqrt 3 }}{2}y = \cos \alpha .$

Phương trình tương đương $\frac{8}{{3\sqrt 3 }}{\cos ^3}\alpha – \frac{2}{{\sqrt 3 }}\cos \alpha – 1 = 0$ $\Leftrightarrow \cos 3\alpha = \frac{{3\sqrt 3 }}{2}$ (vô nghiệm).

Do đó $\left| y \right| \ge \frac{2}{{\sqrt 3 }}$. Như vậy luôn tồn tại $t$ thỏa $y = \frac{1}{{\sqrt 3 }}\left( {t + \frac{1}{t}} \right)$ $(*).$ Thế vào $(1)$ ta được phương trình $\frac{{{t^3}}}{{3\sqrt 3 }} + \frac{1}{{3\sqrt 3 {t^3}}} – 1 = 0$, việc giải phương trình này không khó, xin dành cho bạn đọc.

Ta tìm được nghiệm: $x = \frac{1}{{\sqrt 3 }}\left[ {\sqrt[3]{{\frac{1}{2}\left( {3\sqrt 3 – \sqrt {23} } \right)}} + \frac{1}{{\sqrt[3]{{\frac{1}{2}\left( {3\sqrt 3 – \sqrt {23} } \right)}}}}} \right] – 1.$

Nhận xét: Câu hỏi đặt ra là: “Sử dụng phương pháp trên như thế nào?”. Muốn trả lời, ta cần làm sáng tỏ hai vấn đề:

+ Vấn đề 1. Có luôn tồn tại $t$ thoả mãn cách đặt trên?

Đáp án là không. Coi $(*)$ là phương trình bậc hai theo $t$ ta sẽ tìm được điều kiện $\left| y \right| \ge \frac{2}{{\sqrt 3 }}.$ Thật ra có thể tìm nhanh bằng cách dùng bất đẳng thức AM – GM: $\left| y \right| = \left| {\frac{1}{{\sqrt 3 }}\left( {t + \frac{1}{t}} \right)} \right|$ $= \frac{1}{{\sqrt 3 }}\left( {\left| t \right| + \frac{1}{{\left| t \right|}}} \right) \ge \frac{2}{{\sqrt 3 }}.$

Vậy trước hết ta phải chứng minh $(1)$ không có nghiệm $\left| y \right| < \frac{2}{{\sqrt 3 }}.$

+ Vấn đề 2. Vì sao có số $\frac{2}{{\sqrt 3 }}$?

Ý tưởng của ta là từ phương trình $x^3+px+q=0$ đưa về một phương trình trùng phương theo $t^3$ qua cách đặt $x = k\left( {t + \frac{1}{t}} \right).$ Khai triển và đồng nhất hệ số ta được $k = \sqrt {\frac{{ – p}}{3}} .$

Sau đây là phương trình dạng $x^3+px+q=0$ với $p < 0$ và có $3$ nghiệm thực:

<!-- chunk:5 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-3-tong-quat.html -->
## Ví dụ 4. Giải phương trình: ${x^3} – {x^2} – 2x + 1 = 0.$

Đặt $y = x – \frac{1}{3}$, ta được phương trình: ${y^3} – \frac{7}{3}y + \frac{7}{{27}} = 0$ $(*).$

Với $\left| y \right| < \frac{{2\sqrt 7 }}{3}$ thì $\left| {\frac{{3y}}{{2\sqrt 7 }}} \right| < 1$, do đó tồn tại $\alpha \in \left[ {0;\pi } \right]$ sao cho $\cos \alpha = \frac{{3y}}{{2\sqrt 7 }}$ hay $y = \frac{{2\sqrt 7 \cos \alpha }}{3}.$

Thế vào $(*)$, ta được: $\cos 3\alpha = – \frac{{\sqrt 7 }}{{14}}$, đây là phương trình lượng giác cơ bản.

Dễ dàng tìm được ba nghiệm của phương trình ban đầu: ${x_1} = \frac{{2\sqrt 7 }}{3}\cos \left[ {\frac{{\arccos \left( { – \frac{{\sqrt 7 }}{{14}}} \right)}}{3}} \right] + \frac{1}{3}$, ${x_{2,3}} = \frac{{2\sqrt 7 }}{3}\cos \left[ {\frac{{ \pm \arccos \left( { – \frac{{\sqrt 7 }}{{14}}} \right)}}{3} + \frac{{2\pi }}{3}} \right] + \frac{1}{3}.$

Do phương trình bậc ba có tối đa $3$ nghiệm phân biệt nên ta không cần xét trường hợp $\left| y \right| \ge \frac{{2\sqrt 7 }}{3}.$

Nhận xét: Ta cũng có thể chứng minh phương trình vô nghiệm khi $\left| y \right| \ge \frac{{2\sqrt 7 }}{3}$ bằng cách đặt $y = \frac{{\sqrt 7 }}{3}\left( {t + \frac{1}{t}} \right)$ giống như ví dụ 3, từ đó dẫn tới một phương trình trùng phương vô nghiệm.

Tổng kết lại, ta dùng phép đặt ẩn phụ $y = \sqrt {\frac{{ – p}}{3}} \left( {t + \frac{1}{t}} \right)$ $(*)$ như sau:

+ Nếu phương trình có $1$ nghiệm thực, chứng minh phương trình vô nghiệm khi $\left| y \right| < 2\sqrt {\frac{{ – p}}{3}}$, trường hợp còn lại dùng $(*)$ để đưa về phương trình trùng phương theo $t.$

+ Nếu phương trình có $3$ nghiệm thực, chứng minh phương trình vô nghiệm khi $\left| y \right| \ge 2\sqrt {\frac{{ – p}}{3}}$ bằng phép đặt $(*)$ (đưa về phương trình trùng phương vô nghiệm theo $t$). Khi $\left| y \right| \le 2\sqrt {\frac{{ – p}}{3}}$ thì đặt $\frac{{\left| y \right|}}{{2\sqrt {\frac{{ – p}}{3}} }} = \cos \alpha$, từ đó tìm $α$, suy ra $3$ nghiệm $y.$

Còn khi $p>0$ không khó chứng minh phương trình có nghiệm duy nhất:

<!-- chunk:6 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-3-tong-quat.html -->
## Ví dụ 5. Giải phương trình: ${x^3} + 6x + 4 = 0.$

Ý tưởng: Ta sẽ dùng phép đặt $x = k\left( {t – \frac{1}{t}} \right)$ để đưa về phương trình trùng phương. Để ý phép đặt này không cần điều kiện của $x$, vì nó tương đương $k\left( {{t^2} – 1} \right) – xt = 0.$ Phương trình trên luôn có nghiệm theo $t$.

Như vậy từ phương trình đầu ta được: ${k^3}\left( {{t^3} – \frac{1}{{{t^3}}}} \right) – 3{k^3}\left( {t – \frac{1}{t}} \right)$ $+ 6k\left( {t – \frac{1}{t}} \right) + 4 = 0.$

Cần chọn $k$ thỏa $3{k^3} = 6k$ $\Rightarrow k = \sqrt 2 .$

Vậy ta có lời giải bài toán như sau:

Đặt $x = \sqrt 2 \left( {t – \frac{1}{t}} \right)$, ta có phương trình: $2\sqrt 2 \left( {{t^3} – \frac{1}{{{t^3}}}} \right) + 4 = 0$ $\Leftrightarrow {t^6} – 1 + \sqrt 2 {t^3} = 0$ $\Leftrightarrow {t_{1,2}} = \sqrt[3]{{\frac{{ – 1 \pm \sqrt 3 }}{{\sqrt 2 }}}}.$

Lưu ý rằng ${t_1}{t_2} = – 1$ theo định lí Vi-ét nên ta chỉ nhận được một giá trị của $x$ là: $x = {t_1} + {t_2}$ $= \sqrt 2 \left( {\sqrt[3]{{\frac{{ – 1 + \sqrt 3 }}{{\sqrt 2 }}}} + \sqrt[3]{{\frac{{ – 1 – \sqrt 3 }}{{\sqrt 2 }}}}} \right).$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-3-tong-quat.html -->
## Ví dụ 6. Giải phương trình $4{x^3} – 3x = m$ với $\left| m \right| > 1.$

Nhận xét rằng khi $\left| x \right| \le 1$ thì $\left| {VT} \right| \le 1 < \left| m \right|$ (sai) nên $\left| x \right| \ge 1.$ Vì vậy ta có thể đặt $x = \frac{1}{2}\left( {t + \frac{1}{t}} \right)$, ta được phương trình: $\frac{1}{2}\left( {{t^3} + \frac{1}{{{t^3}}}} \right) = m.$

Từ đó: $t = \sqrt[3]{{m \pm \sqrt {{m^2} – 1} }}$ $\Rightarrow x = \frac{1}{2}\left( {\sqrt[3]{{m + \sqrt {{m^2} – 1} }} + \sqrt[3]{{m – \sqrt {{m^2} – 1} }}} \right).$

Ta chứng minh đây là nghiệm duy nhất của phương trình.

Giả sử phương trình có nghiệm ${x_0}$ thì ${x_0} \notin \left[ { – 1;1} \right]$ vì $\left| {{x_0}} \right| > 1.$ Khi đó: $4{x^3} – 3x = 4x_0^3 – 3{x_0}$ $\Leftrightarrow \left( {x – {x_0}} \right)\left( {4{x^2} + 4x{x_0} + 4x_0^2 – 3} \right) = 0.$

Xét phương trình: $4{x^2} + 4x{x_0} + 4x_0^2 – 3 = 0.$

Ta có: $\Delta ‘ = 12 – 12x_0^2 < 0$ nên phương trình bậc hai này vô nghiệm.

Vậy phương trình đã cho có nghiệm duy nhất là: $x = \frac{1}{2}\left( {\sqrt[3]{{m + \sqrt {{m^2} – 1} }} + \sqrt[3]{{m – \sqrt {{m^2} – 1} }}} \right).$