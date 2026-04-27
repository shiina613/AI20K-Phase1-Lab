# Chứng minh công thức lượng giác bằng số phức

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/chung-minh-cong-thuc-luong-giac-bang-so-phuc.html -->
**Có thể bạn chưa biết?**

Ta đã làm quen với các công thức lượng giác từ chương trình Toán lớp 11, tuy nhiên có thể nhiều người trong chúng ta chưa biết cách chứng minh các công thức lượng giác đó như thế nào, vì thế trong chủ đề này, chúng ta sẽ đề cập tới một cách chứng minh các công thức lượng giác có sử dụng số phức, hay cụ thể hơn là công thức Euler.

<img link="data_for_rag/toan12/images/chung-minh-cong-thuc-luong-giac-bang-so-phuc-296x300.png" alt="">

*Nhà toán học Leonhard Euler*

Ta có công thức rất nổi tiếng do nhà toán học Euler phát biểu như sau: ${e^{i\varphi }} = \cos \varphi + i\sin \varphi$ (việc chứng minh công thức này sẽ được đề cập tới trong một bài viết khác).

Bây giờ áp dụng công thức này với các biểu thức lượng giác nhân đôi, nhân ba thì ta có:

${e^{i.(2a)}} = \cos 2a + i\sin 2a.$

${e^{i(a + a)}} = {(\cos a + i\sin a)^2}$ $= {\cos ^2}a – {\sin ^2}a + 2i\cos a\sin a.$

Đến đây đồng nhất hệ số hai vế ta sẽ thu được công thức góc nhân đôi là:

$\cos 2a = {\cos ^2}a – {\sin ^2}a.$

$\sin 2a = 2\sin a.\cos a.$

Với công thức nhân ba thì cũng tương tự, ta có:

${e^{i(3a)}} = \cos 3a + i\sin 3a.$

${e^{i(3a)}} = {\left( {{e^a}} \right)^3}$ $= {(\cos a + i\sin a)^3}$ $= {\cos ^3}a + 3i{\cos ^2}a – 3\cos a.{\sin ^2}a – i{\sin ^3}a.$

Đến đây ta cũng đồng nhất hệ số như trên và sử dụng công thức lượng giác quen thuộc ${\sin ^2}x + {\cos ^2}x = 1$ thì ta cũng thu được hai công thức nhân ba như ta đã biết.

Tiếp theo ứng dụng công thức Euler, ta có biến đổi sau:

${e^{i(a + b)}}$ $= \cos (a + b) + i\sin (a + b)$   $(1).$

${e^{ia}}.{e^{ib}}$ $= [\cos a + i\sin a][\cos b + i\sin b].$

$= \cos a.\cos b – \sin a.\sin b$ $+ i(\sin a\cos b + \cos a\sin b)$   $(2).$

Đồng nhất hệ số ở hai đẳng thức $(1)$ và $(2)$ ta thu được hai công thức lượng giác quen thuộc:

$\cos (a + b)$ $= \cos a.\cos b – \sin a.\sin b.$

$\sin (a + b)$ $= \sin a.\cos b + \cos a.\sin b.$

Tương tự cho công thức hiệu, ta có:

${e^{i(a – b)}}$ $= \cos (a – b) + i\sin (a – b).$

$\frac{{{e^{ia}}}}{{{e^{ib}}}} = \frac{{\cos a + i\sin a}}{{\cos b + i\sin b}}.$

$= \frac{{(\cos a + i\sin a)(\cos b – i\sin b)}}{{{{\cos }^2}b + {{\sin }^2}b}}.$

$= \cos a\cos b + \sin a\sin b$ $+ i(\sin a\cos b – \cos a\sin b).$

Vậy câu hỏi đặt ra là với công thức biến tổng thành tích thì ta sẽ làm như thế nào?

Trước tiên ta có:

${e^{ia}} = \cos a + i\sin a$   $(3).$

${e^{ib}} = \cos b + i\sin b$   $(4).$

Tiếp theo ta lại có:

${e^{i\left( {\frac{{a + b}}{2}} \right)}}.{e^{i\left( {\frac{{a – b}}{2}} \right)}}$ $= \left( {\cos \frac{{a + b}}{2} + i\sin \frac{{a + b}}{2}} \right)\left( {\cos \frac{{a – b}}{2} + i\sin \frac{{a – b}}{2}} \right).$

$= \cos \frac{{a + b}}{2}.\cos \frac{{a – b}}{2}$ $– \sin \frac{{a + b}}{2}.\sin \frac{{a – b}}{2}$ $+ i\left( {\sin \frac{{a + b}}{2}.\cos \frac{{a – b}}{2} + \cos \frac{{a + b}}{2}.\sin \frac{{a – b}}{2}} \right).$   $(5).$

${e^{i\left( {\frac{{a + b}}{2}} \right)}}.{e^{i\left( {\frac{{b – a}}{2}} \right)}}$ $= \left( {\cos \frac{{a + b}}{2} + i\sin \frac{{a + b}}{2}} \right)\left( {\cos \frac{{b – a}}{2} + i\sin \frac{{b – a}}{2}} \right).$

$= \cos \frac{{a + b}}{2}.\cos \frac{{a – b}}{2}$ $+ \sin \frac{{a + b}}{2}.\sin \frac{{a – b}}{2}$ $+ i\left( {\sin \frac{{a + b}}{2}.\cos \frac{{a – b}}{2} – \cos \frac{{a + b}}{2}.\sin \frac{{a – b}}{2}} \right)$   $(6).$

Bây giờ lấy $(3)$ cộng (hoặc trừ) với $(4)$ và $(5)$ cộng (hoặc trừ) với $(6)$ ta có ngay các đẳng thức lượng giác quen thuộc. Từ công thức này ta suy ra công thức biến tích thành tổng.

Ngoài ra các công thức liên quan tới các hàm $\tan x$ và $\cot x$ ta cũng sử dụng các biến đổi đại số thuần túy và các công thức đã chứng minh ở trên để suy ra nó. Các bạn cũng có thể từ công thức Euler để suy ra các đẳng thức lượng giác khác phong phú hơn.

Cuối cùng mình xin kết thúc bài viết này tại đây, bài viết sau sẽ đề cập tới cách chứng minh công thức Euler, mong các bạn đón đọc!

*Tác giả: **Nguyễn Minh Tuấn** (Tạp chí và Tư liệu Toán học)*