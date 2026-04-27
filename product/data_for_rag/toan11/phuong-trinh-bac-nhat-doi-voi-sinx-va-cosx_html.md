# Phương trình bậc nhất đối với sinx và cosx

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
Bài viết hướng dẫn phương pháp giải và biện luận phương trình bậc nhất đối với sinx và cosx.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## I. PHƯƠNG PHÁP

Bài toán: Giải và biện luận phương trình: $a\sin x + b\cos x = c$ $(1).$

PHƯƠNG PHÁP CHUNG:

Ta có thể lựa chọn một trong các cách sau:

Cách 1: Thực hiện theo các bước:

+ Bước 1. Kiểm tra:

1. Nếu ${a^2} + {b^2} < {c^2}$ phương trình vô nghiệm.

2. Nếu ${a^2} + {b^2} \ge {c^2}$, khi đó để tìm nghiệm của phương trình $(1)$ ta thực hiện tiếp bước 2.

+ Bước 2. Chia hai vế phương trình $(1)$ cho $\sqrt {{a^2} + {b^2}}$, ta được:

$\frac{a}{{\sqrt {{a^2} + {b^2}} }}\sin x + \frac{b}{{\sqrt {{a^2} + {b^2}} }}\cos x$ $= \frac{c}{{\sqrt {{a^2} + {b^2}} }}.$

Vì ${\left( {\frac{a}{{\sqrt {{a^2} + {b^2}} }}} \right)^2} + {\left( {\frac{b}{{\sqrt {{a^2} + {b^2}} }}} \right)^2} = 1$ nên tồn tại góc $\beta$ sao cho $\frac{a}{{\sqrt {{a^2} + {b^2}} }} = \cos \beta$, $\frac{b}{{\sqrt {{a^2} + {b^2}} }} = \sin \beta .$

Khi đó phương trình $(1)$ có dạng:

$\sin x\cos \beta + \sin \beta \cos x = \frac{c}{{\sqrt {{a^2} + {b^2}} }}$ $\Leftrightarrow \sin (x + \beta ) = \frac{c}{{\sqrt {{a^2} + {b^2}} }}.$

Đây là phương trình cơ bản của sin.

Cách 2: Thực theo các bước:

+ Bước 1. Với $\cos \frac{x}{2} = 0$ $\Leftrightarrow x = \pi + 2k\pi$, kiểm tra vào phương trình.

+ Bước 2. Với $\cos \frac{x}{2} \ne 0$ $\Leftrightarrow x \ne \pi + 2k\pi$, đặt $t = \tan \frac{x}{2}$, suy ra:

$\sin x = \frac{{2t}}{{1 + {t^2}}}$ và $\cos x = \frac{{1 – {t^2}}}{{1 + {t^2}}}.$

Khi đó phương trình $(1)$ có dạng:

$a.\frac{{2t}}{{1 + {t^2}}} + b.\frac{{1 – {t^2}}}{{1 + {t^2}}} = c$ $\Leftrightarrow (c + b){t^2} – 2at + c – b = 0$ $(2).$

+ Bước 3. Giải phương trình $(2)$ theo $t.$

Cách 3: Với những yêu cầu biện luận số nghiệm của phương trình trong $(\alpha ,\beta )$, ta có thể lựa chọn phương pháp hàm số đồ thị.

Cách 4: Với những yêu cầu biện luận tính chất nghiệm của phương trình trong $(\alpha ,\beta )$, ta có thể lựa chọn phương pháp điều kiện cần và đủ.

Nhận xét quan trọng:

1. Cách 1 thường được sử dụng với các bài toán yêu cầu giải phương trình và tìm điều kiện của tham số để phương trình có nghiệm, vô nghiệm hoặc giải và biện luận phương trình theo tham số.

2. Cách 2 thường được sử dụng với các bài toán yêu cầu giải phương trình và tìm điều kiện của tham số để phương trình có nghiệm thuộc tập $D$ với $D \subset [0,2\pi ].$

3. Cách 3 thường được sử dụng với các bài toán yêu cầu biện luận theo tham số để phương trình có $k$ nghiệm thuộc tập $D$ với $D \cap [0,2\pi ] \ne \emptyset .$

4. Từ cách giải 1 ta có được kết quả sau:

$– \sqrt {{a^2} + {b^2}}$ $\le a\sin x + b\cos x$ $\le \sqrt {{a^2} + {b^2}} .$

Kết quả đó gợi ý cho bài toán về giá trị lớn nhất và nhỏ nhất của các hàm số dạng $y = a\sin x + b\cos x$, $y = \frac{{a\sin x + b\cos x}}{{c\sin x + d\cos x}}$ và phương pháp đánh giá cho một số phương trình lượng giác.

Dạng đặc biệt:

+ $\sin x + \cos x = 0$ $\Leftrightarrow x = – \frac{\pi }{4} + k\pi$, $k \in Z.$

+ $\sin x – \cos x = 0$ $\Leftrightarrow x = \frac{\pi }{4} + k\pi$, $k \in Z.$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 1: Giải phương trình: $\sqrt 3 \sin 3x + \cos 3x = \sqrt 2 .$

Biến đổi phương trình về dạng:

$\frac{{\sqrt 3 }}{2}\sin 3x + \frac{1}{2}\cos 3x = \frac{{\sqrt 2 }}{2}$ $\Leftrightarrow \sin 3x\cos \frac{\pi }{6} + \cos 3x\sin \frac{\pi }{6} = \frac{{\sqrt 2 }}{2}$ $\Leftrightarrow \sin \left( {3x + \frac{\pi }{6}} \right) = \sin \frac{\pi }{4}$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{3x + \frac{\pi }{6} = \frac{\pi }{4} + 2k\pi }\\
{3x + \frac{\pi }{6} = \pi – \frac{\pi }{4} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{{36}} + \frac{{2k\pi }}{3}}\\
{x = \frac{{7\pi }}{{36}} + \frac{{2k\pi }}{3}}
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

<!-- chunk:3 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 2: Giải phương trình: $3\sin x – 4\cos x = – \frac{5}{2}.$

Biến đổi phương trình về dạng:

$\frac{3}{5}\sin x – \frac{4}{5}\cos x = – \frac{1}{2}.$

Đặt $\frac{3}{5} = \cos \alpha$ và $\frac{4}{5} = \sin \alpha$, khi đó ta được:

$\sin x\cos \alpha – \cos x\sin \alpha = – \frac{1}{2}$ $\Leftrightarrow \sin (x – \alpha ) = \sin \left( { – \frac{\pi }{6}} \right)$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x – \alpha = – \frac{\pi }{6} + 2k\pi }\\
{x – \alpha = \pi + \frac{\pi }{6} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \alpha – \frac{\pi }{6} + 2k\pi }\\
{x = \frac{{5\pi }}{6} + \alpha + 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 3: Giải phương trình: $\sin 2x – 3\cos 2x = 3.$

Ta có thể lựa chọn một trong hai cách sau:

Cách 1: Biến đổi phương trình về dạng:

$\frac{1}{{\sqrt {10} }}\sin 2x – \frac{3}{{\sqrt {10} }}\cos 2x = \frac{3}{{\sqrt {10} }}.$

Đặt $\frac{1}{{\sqrt {10} }} = \cos \alpha$ và $\frac{3}{{\sqrt {10} }} = \sin \alpha$, khi đó ta được:

$\sin 2x\cos \alpha – \cos 2x\sin \alpha = \sin \alpha$ $\Leftrightarrow \sin (2x – \alpha ) = \sin \alpha$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{2x – \alpha = \alpha + 2k\pi }\\
{2x – \alpha = \pi – \alpha + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \alpha + k\pi }\\
{x = \frac{\pi }{2} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

Cách 2: Biến đổi phương trình về dạng:

$\sin 2x = 3(1 + \cos 2x)$ $\Leftrightarrow 2\sin x\cos x = 6{\cos ^2}x$ $\Leftrightarrow (\sin x – 3\cos x)\cos x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin x – 3\cos x = 0}\\
{\cos x = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = 3 = \tan \alpha }\\
{\cos x = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \alpha + k\pi }\\
{x = \frac{\pi }{2} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

<!-- chunk:5 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 4: Giải phương trình: $2\sin x – 3\cos x = – 2.$

Ta có thể lựa chọn một trong hai cách sau:

Cách 1: Biến đổi phương trình về dạng:

$\frac{2}{{\sqrt {13} }}\sin x – \frac{3}{{\sqrt {13} }}\cos x = – \frac{2}{{\sqrt {13} }}.$

Đặt $\frac{2}{{\sqrt {13} }} = \cos \alpha$ và $\frac{3}{{\sqrt {13} }} = \sin \alpha$, khi đó ta được:

$\sin x\cos \alpha – \cos x\sin \alpha = – \cos \alpha$ $\Leftrightarrow \sin (x – \alpha ) = \sin \left( {\alpha – \frac{\pi }{2}} \right)$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x – \alpha = \alpha – \frac{\pi }{2} + 2k\pi }\\
{x – \alpha = \pi – \alpha + \frac{\pi }{2} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 2\alpha – \frac{\pi }{2} + 2k\pi }\\
{x = \frac{{3\pi }}{2} + 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

Cách 2: Biến đổi phương trình về dạng:

$2(1 + \sin x) = 3\cos x$ $\Leftrightarrow 2{\left( {\cos \frac{x}{2} + \sin \frac{x}{2}} \right)^2}$ $= 3\left( {{{\cos }^2}\frac{x}{2} – {{\sin }^2}\frac{x}{2}} \right).$

$\Leftrightarrow \left[ {2\left( {\cos \frac{x}{2} + \sin \frac{x}{2}} \right) – 3\left( {\cos \frac{x}{2} – \sin \frac{x}{2}} \right)} \right]\left( {\cos \frac{x}{2} + \sin \frac{x}{2}} \right) = 0.$
\Leftrightarrow \left[ {\begin{array}{l}
{5\sin \frac{x}{2} – \cos \frac{x}{2} = 0}\\
{\cos \frac{x}{2} + \sin \frac{x}{2} = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan \frac{x}{2} = \frac{1}{5} = \tan \alpha }\\
{\tan \frac{x}{2} = – 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\frac{x}{2} = \alpha + k\pi }\\
{\frac{x}{2} = \frac{{3\pi }}{4} + k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 2\alpha + 2k\pi }\\
{x = \frac{{3\pi }}{2} + 2k\pi }
\end{array}} \right.
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

Chú ý: Các em học sinh cần có thói quen kiểm tra điều kiện ${a^2} + {b^2} \ge {c^2}$ ra nháp trước khi đi giải phương trình bởi có nhiều bài thi đã cố tình tạo ra những phương trình không thoả mãn điều kiện trên với mục đích kiểm tra kiến thức cơ bản của các em. Cụ thể như đề thi ĐHGTVT – 2000.

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 5: (ĐHGTVT – 2000): Giải phương trình: $2\sqrt 2 (\sin x + \cos x)\cos x = 3 + \cos 2x.$

Biến đổi phương trình về dạng:

$\sqrt 2 \sin 2x + \sqrt 2 (1 + \cos 2x) = 3 + \cos 2x$ $\Leftrightarrow \sqrt 2 \sin 2x + (\sqrt 2 – 1)\cos 2x = 3 – \sqrt 2 .$

Ta có:
\left\{ {\begin{array}{l}
{a = \sqrt 2 }\\
{b = \sqrt 2 – 1}\\
{c = 3 – \sqrt 2 }
\end{array}} \right.
$$
 
$$
\Rightarrow \left( {\begin{array}{l}
{{a^2} + {b^2} = 2 + {{(\sqrt 2 – 1)}^2} = 5 – 2\sqrt 2 }\\
{{c^2} = {{(3 – \sqrt 2 )}^2} = 11 – 6\sqrt 2 }
\end{array}} \right.
$\Rightarrow {a^2} + {b^2} < {c^2}.$

Vậy phương trình vô nghiệm.

***Chú ý***: Việc lựa chọn các phép biến đổi lượng giác phù hợp trong nhiều trường hợp ta sẽ tìm được phép biểu diễn chẵn cho các họ nghiệm. Chúng ta xem xét ví dụ sau:

<!-- chunk:7 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 6: Giải phương trình: $(1 + \sqrt 3 )\sin x + (1 – \sqrt 3 )\cos x = 2.$

Cách 1: Biến đổi phương trình về dạng:

$\frac{{1 + \sqrt 3 }}{{2\sqrt 2 }}\sin x + \frac{{1 – \sqrt 3 }}{{2\sqrt 2 }}\cos x = \frac{1}{{\sqrt 2 }}.$

Đặt $\frac{{1 + \sqrt 3 }}{{2\sqrt 2 }} = \cos \alpha$ thì $\frac{{1 – \sqrt 3 }}{{2\sqrt 2 }} = \sin \alpha$, khi đó ta được:

$\sin x\cos \alpha + \cos x\sin \alpha = \frac{1}{{\sqrt 2 }}$ $\Leftrightarrow \sin (x + \alpha ) = \sin \frac{\pi }{4}.$
\Leftrightarrow \left[ {\begin{array}{l}
{x + \alpha = \frac{\pi }{4} + 2\dot k\pi }\\
{x + \alpha = \pi – \frac{\pi }{4} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{4} – \alpha + 2k\pi }\\
{x = \frac{{3\pi }}{4} – \alpha + 2k\pi }
\end{array}} \right.
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

Cách 2: Biến đổi phương trình về dạng:

$(\sin x + \cos x) + \sqrt 3 (\sin x – \cos x) = 2$ $\Leftrightarrow \sqrt 2 \sin \left( {x + \frac{\pi }{4}} \right)$ $– \sqrt 6 \cos \left( {x + \frac{\pi }{4}} \right) = 2$ $\Leftrightarrow \frac{1}{2}\sin \left( {x + \frac{\pi }{4}} \right)$ $– \frac{{\sqrt 3 }}{2}\cos \left( {x + \frac{\pi }{4}} \right) = \frac{1}{{\sqrt 2 }}$ $\Leftrightarrow \sin \left( {x + \frac{\pi }{4}} \right)\cos \frac{\pi }{3}$ $– \cos \left( {x + \frac{\pi }{4}} \right)\sin \frac{\pi }{3} = \frac{1}{{\sqrt 2 }}$ $\Leftrightarrow \sin \left( {x + \frac{\pi }{4} – \frac{\pi }{3}} \right) = \sin \frac{\pi }{4}$
\Leftrightarrow \left[ {\begin{array}{l}
{x – \frac{\pi }{{12}} = \frac{\pi }{4} + 2k\pi }\\
{x – \frac{\pi }{{12}} = \pi – \frac{\pi }{4} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{3} + 2k\pi }\\
{x = \frac{{5\pi }}{6} + 2k\pi }
\end{array}} \right.
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

Nhận xét:

Như vậy bằng cách 1 ta tìm được nghiệm của phương trình không tường minh, trong khi đó nếu sử dụng cách 2 ta thấy nghiệm của phương trình rất chẵn.

Một vài tài liệu tham khảo giải phương trình bằng cách đặt $t = \tan \frac{x}{2}$, dẫn tới phương trình:

$(3 – \sqrt 3 ){t^2} – 2(1 + \sqrt 3 )t + \sqrt 3 + 1 = 0$ $\Leftrightarrow {t_1} = \frac{1}{{\sqrt 3 }} \vee {t_2} = \frac{{\sqrt 3 + 1}}{{\sqrt 3 – 1}}.$

+ Với ${t_1} = \frac{1}{{\sqrt 3 }}$ ta được:

$\tan \frac{x}{2} = \frac{1}{{\sqrt 3 }} = \tan \frac{\pi }{6}$ $\Leftrightarrow \frac{x}{2} = \frac{\pi }{6} + k\pi$ $\Leftrightarrow x = \frac{\pi }{3} + 2k\pi$, $k \in Z.$

+ Với ${t_2} = \frac{{\sqrt 3 + 1}}{{\sqrt 3 – 1}}$ ta được:

$\tan \frac{x}{2} = \frac{{\sqrt 3 + 1}}{{\sqrt 3 – 1}}$ $= – \frac{{\tan \frac{\pi }{3} + \tan \frac{\pi }{4}}}{{1 – \tan \frac{\pi }{3}.\tan \frac{\pi }{4}}}$ $= – \tan \frac{{7\pi }}{{12}}$ $= \tan \frac{{5\pi }}{{12}}.$

$\Leftrightarrow \frac{x}{2} = \frac{{5\pi }}{{12}} + k\pi$ $\Leftrightarrow x = \frac{{5\pi }}{6} + 2k\pi$, $k \in Z.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 7: Giải phương trình: $2(\sqrt 3 \sin x – \cos x)$ $= 3\sin 2x + \sqrt 7 \cos 2x.$

Biến đổi phương trình về dạng:

$2\sqrt 3 \sin x – 2\cos x$ $= 3\sin 2x + \sqrt 7 \cos 2x$ $\Leftrightarrow \frac{{\sqrt 3 }}{2}\sin x – \frac{1}{2}\cos x$ $= \frac{3}{4}\sin 2x + \frac{{\sqrt 7 }}{4}\cos 2x.$

Đặt $\frac{3}{4} = \cos \alpha$ và $\frac{{\sqrt 7 }}{4} = \sin \alpha$, khi đó ta được:

$\sin x\cos \frac{\pi }{6} – \cos x\sin \frac{\pi }{6}$ $= \sin 2x\cos \alpha + \cos 2x\sin \alpha$ $\Leftrightarrow \sin \left( {x – \frac{\pi }{6}} \right) = \sin (2x + \alpha )$
\Leftrightarrow \left[ {\begin{array}{l}
{2x + \alpha = x – \frac{\pi }{6} + 2k\pi }\\
{2x + \alpha = \pi – x + \frac{\pi }{6} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{6} – \alpha + 2k\pi }\\
{x = \frac{{7\pi }}{{18}} – \frac{\alpha }{3} + \frac{{2k\pi }}{3}}
\end{array}} \right.
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

Chú ý: Ví dụ trên đã minh hoạ cụ thể phương pháp giải phương trình dạng: $a\sin (kx) + b\cos (kx)$ $= c\sin (lx) + d\cos (lx)$  $(I)$, với điều kiện ${a^2} + {b^2} = {c^2} + {d^2}.$

Và sự mở rộng khác cho dạng phương trình trên như sau: $a\sin (kx) + b\cos (kx)$ $= \sqrt {{a^2} + {b^2}} \sin (lx)$ $(II).$

Để minh hoạ ta xem xét ví dụ sau:

<!-- chunk:9 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 8: Giải phương trình: $2\sin x(\cos x – 1) = \sqrt 3 \cos 2x.$

Biến đổi phương trình về dạng:

$2\sin x\cos x – 2\sin x = \sqrt 3 \cos 2x$ $\Leftrightarrow \sin 2x – \sqrt 3 \cos 2x = 2\sin x$ $(*).$

$\Leftrightarrow \frac{1}{2}\sin 2x – \frac{{\sqrt 3 }}{2}\cos 2x = \sin x$ $\Leftrightarrow \sin 2x\cos \frac{\pi }{3} – \cos 2x\sin \frac{\pi }{3} = \sin x.$

$\Leftrightarrow \sin \left( {2x – \frac{\pi }{3}} \right) = \sin x$
\Leftrightarrow \left[ {\begin{array}{l}
{2x – \frac{\pi }{3} = x + 2k\pi }\\
{2x – \frac{\pi }{3} = \pi – x + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{3} + 2k\pi }\\
{x = \frac{{4\pi }}{9} + \frac{{2k\pi }}{3}}
\end{array}} \right.
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

Nhận xét: Như vậy bằng một vài phép biến đổi lượng giác thông thường ta đã chuyển phương trình ban đầu về $(*)$ và đó chính là dạng $(II).$

<!-- chunk:10 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 9: Giải phương trình:

$\sqrt 2 (\sin x + \sqrt 3 \cos x)$ $= \sqrt 3 \cos 2x – \sin 2x.$

Biến đổi phương trình về dạng:

$\sqrt 2 \left( {\frac{1}{2}\sin x + \frac{{\sqrt 3 }}{2}\cos x} \right)$ $= \frac{{\sqrt 3 }}{2}\cos 2x – \frac{1}{2}\sin 2x.$

$\Leftrightarrow \sqrt 2 \left( {\sin x\cos \frac{\pi }{3} + \cos x\sin \frac{\pi }{3}} \right)$ $= \sin \frac{\pi }{3}\cos 2x – \cos \frac{\pi }{3}\sin 2x.$

$\Leftrightarrow \sqrt 2 \sin \left( {x + \frac{\pi }{3}} \right)$ $= \sin \left( {\frac{\pi }{3} – 2x} \right)$ $= \sin \left( {2x + \frac{{2\pi }}{3}} \right).$

$\Leftrightarrow \sqrt 2 \sin \left( {x + \frac{\pi }{3}} \right)$ $= 2\sin \left( {x + \frac{\pi }{3}} \right)\cos \left( {x + \frac{\pi }{3}} \right).$

$\Leftrightarrow \left[ {\sqrt 2 – 2\cos \left( {x + \frac{\pi }{3}} \right)} \right]\sin \left( {x + \frac{\pi }{3}} \right) = 0.$
\Leftrightarrow \left[ {\begin{array}{l}
{\cos \left( {x + \frac{\pi }{3}} \right) = \frac{{\sqrt 2 }}{2}}\\
{\sin \left( {x + \frac{\pi }{3}} \right) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x + \frac{\pi }{3} = \pm \frac{\pi }{4} + 2k\pi }\\
{x + \frac{\pi }{3} = k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{{12}} + 2k\pi }\\
{x = – \frac{{7\pi }}{{12}} + 2k\pi }\\
{x = – \frac{\pi }{3} + k\pi }
\end{array}} \right.
, $k \in Z.$

Vậy phương trình có ba họ nghiệm.

<!-- chunk:11 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 10: Cho phương trình: $\sqrt 3 \sin 2x – m\cos 2x = 1.$

a. Giải phương trình với $m = 1.$

b. Chứng tỏ rằng phương trình có nghiệm với mọi $m.$

Với $m = 1$, phương trình có dạng:

$\sqrt 3 \sin 2x – m\cos 2x = 1$ $\Leftrightarrow \frac{{\sqrt 3 }}{2}\sin 2x – \frac{1}{2}\cos 2x = \frac{1}{2}.$

$\Leftrightarrow \sin 2x\cos \frac{\pi }{6} – \cos 2x\sin \frac{\pi }{6} = \frac{1}{2}$ $\Leftrightarrow \sin \left( {2x – \frac{\pi }{6}} \right) = \sin \frac{\pi }{6}.$
\Leftrightarrow \left[ {\begin{array}{l}
{2x – \frac{\pi }{6} = \frac{\pi }{6} + 2k\pi }\\
{2x – \frac{\pi }{6} = \pi – \frac{\pi }{6} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{6} + k\pi }\\
{x = \frac{\pi }{2} + k\pi }
\end{array}} \right.
, $k \in Z.$

Vậy với $m =1$ phương trình có hai họ nghiệm.

b. Ta có: ${a^2} + {b^2} = 3 + {m^2} > 1 = {c^2}$, $\forall m.$

Vậy phương trình có nghiệm với mọi $m.$

<!-- chunk:12 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 11: (ĐHKT – 2001): Giải và biện luận phương trình:

$4m(\sin x + \cos x)$ $= 4{m^2} + 2(\cos x – \sin x) + 3.$

Biến đổi phương trình về dạng:

$2(2m + 1)\sin x + 2(2m – 1)\cos x$ $= 4{m^2} + 3.$

Xét hiệu:

${a^2} + {b^2} – {c^2}$ $= 4{(2m + 1)^2} + 4{(2m – 1)^2} – {\left( {4{m^2} + 3} \right)^2}$ $= – \left( {16{m^4} – 8{m^2} + 1} \right)$ $= – {\left( {4{m^2} – 1} \right)^2} \le 0.$

Vậy phương trình chỉ có nghiệm $\Leftrightarrow {a^2} + {b^2} – {c^2} = 0$ $\Leftrightarrow m = \pm \frac{1}{2}.$

+ Với $m = \frac{1}{2}$, phương trình có dạng:

$\sin x = 1$ $\Leftrightarrow x = \frac{\pi }{2} + 2k\pi$, $k \in Z.$

+ Với $m = – \frac{1}{2}$, phương trình có dạng:

$\cos x = 1$ $\Leftrightarrow x = 2k\pi$, $k \in Z.$

+ Với $m \ne \pm \frac{1}{2}$, phương trình vô nghiệm.

<!-- chunk:13 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 12: Cho phương trình:

$(m + 2)\sin x – 2m\cos x = 2m + 2$ $(1).$

a. Giải phương trình với $m = -2.$

b. Tìm $m$ để phương trình có nghiệm thuộc $\left[ { – \frac{\pi }{2},0} \right].$

Xét hai trường hợp:

+ Với $\cos \frac{x}{2} = 0$ $\Leftrightarrow \frac{x}{2} = \frac{\pi }{2} + k\pi$ $\Leftrightarrow x = \pi + 2k\pi$, thay vào phương trình ta được:

$(m + 2)\sin (\pi + 2k\pi ) – 2m\cos (\pi + 2k\pi )$ $= 2m + 2$ $\Leftrightarrow 2m = 2m + 2$ (Mâu thuẫn).

Vậy $x = \pi + 2k\pi$, $k \in Z$ không phải là nghiệm của phương trình với mọi $m.$

+ Với $\cos \frac{x}{2} \ne 0$ $\Leftrightarrow \frac{x}{2} \ne \frac{\pi }{2} + k\pi$ $\Leftrightarrow x \ne \pi + 2k\pi$, $k \in Z.$

Đặt $t = \tan \frac{x}{2}$, suy ra: $\sin x = \frac{{2t}}{{1 + {t^2}}}$ và $\cos x = \frac{{1 – {t^2}}}{{1 + {t^2}}}.$

Khi đó phương trình $(1)$ có dạng:

$\frac{{(m + 2)t}}{{1 + {t^2}}} – \frac{{2m\left( {1 – {t^2}} \right)}}{{1 + {t^2}}} = 2m + 2$ $\Leftrightarrow {t^2} – (m + 2)t + 2m + 1 = 0$ $(2).$

a. Với $m = -2$, phương trình $(2)$ có dạng:

${t^2} – 3 = 0$
\Leftrightarrow \left[ {\begin{array}{l}
{t = \sqrt 3 }\\
{t = – \sqrt 3 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan \frac{x}{2} = \sqrt 3 }\\
{\tan \frac{x}{2} = – \sqrt 3 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\frac{x}{2} = \frac{\pi }{3} + k\pi }\\
{\frac{x}{2} = – \frac{\pi }{3} + k\pi }
\end{array}} \right.
$\Leftrightarrow x = \pm \frac{{2\pi }}{3} + 2k\pi$, $k \in Z.$

Vậy với $m = -2$, phương trình có hai họ nghiệm.

b. Vì $x \in \left[ { – \frac{\pi }{2},0} \right]$ $\Leftrightarrow \frac{x}{2} \in \left[ { – \frac{\pi }{4},0} \right]$ suy ra $t \in [ – 1,0].$

Cách 1: Để $(1)$ có nghiệm thuộc $\left[ { – \frac{\pi }{2},0} \right] \Leftrightarrow (2)$ có nghiệm thuộc $[ – 1,0].$

$\Leftrightarrow$
\left[ \begin{array}{l}
\left( 2 \right){\rm{\:có\:1\:nghiệm\:thuộc\:}}[ – 1,0]\\
\left( 2 \right){\rm{\:có\:1\:nghiệm\:thuộc\:}}[ – 1,0]
\end{array} \right..

\Leftrightarrow \left[ {\begin{array}{l}
{f( – 1)f(0) \le 0}\\
{\left\{ {\begin{array}{l}
{\Delta \ge 0}\\
{af( – 1) \ge 0}\\
{af(0) \ge 0}\\
{ – 1 \le \frac{S}{2} \le 0}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\left[ \begin{array}{l}
(3m + 4)(2m + 1) \le 0\\
\left\{ {\begin{array}{l}
{{m^2} – 4m \ge 0}\\
{3m + 4 \ge 0}\\
{2m + 1 \ge 0}\\
{ – 1 \le \frac{{m + 2}}{2} \le 0}
\end{array}} \right.
\end{array} \right.
$\Leftrightarrow – \frac{4}{3} \le m \le – \frac{1}{2}.$

Vậy với $– \frac{4}{3} \le m \le – \frac{1}{2}$ phương trình có nghiệm.

Cách 2: Viết lại phương trình dưới dạng:

$\frac{{{t^2} – 2t + 1}}{{t – 2}} = m.$

Phương trình $(1)$ có nghiệm $\Leftrightarrow$ đường thẳng $y = m$ cắt đồ thị hàm số $y = \frac{{{t^2} – 2t + 1}}{{t – 2}}$ trên đoạn $[ – 1,0].$

Xét hàm số $(C):y = \frac{{{t^2} – 2t + 1}}{{t – 2}}$ trên đoạn $[ – 1,0].$

Đạo hàm:

$y’ = \frac{{{t^2} – 4t + 3}}{{{{(t – 2)}^2}}} > 0$ với mọi $t \in [ – 1,0]$ $\Leftrightarrow$ hàm số đồng biến trên $\left[ { – 1,0} \right].$

Do đó đường thẳng $y = m$ cắt đồ thị hàm số $(C)$ trên đoạn $[ – 1,0].$

$\Leftrightarrow y( – 1) \le m \le y(0)$ $\Leftrightarrow – \frac{4}{3} \le m \le – \frac{1}{2}.$

Vậy với $– \frac{4}{3} \le m \le – \frac{1}{2}$ phương trình có nghiệm.

<!-- chunk:14 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 13: Cho phương trình: $\sqrt 3 \sin x + \cos x = m$ $(1).$

a. Giải phương trình với $m = -1.$

b. Biện luận theo $m$ số nghiệm thuộc $\left( { – \frac{\pi }{6},2\pi } \right]$ của phương trình.

a. Với $m = -1$, phương trình có dạng:

$\sqrt 3 \sin x + \cos x = – 1$ $\Leftrightarrow \frac{{\sqrt 3 }}{2}\sin x + \frac{1}{2}\cos x = – \frac{1}{2}$ $\Leftrightarrow \sin \left( {x + \frac{\pi }{6}} \right) = \sin \left( { – \frac{\pi }{6}} \right).$
\Leftrightarrow \left[ {\begin{array}{c}
{x + \frac{\pi }{6} = – \frac{\pi }{6} + 2k\pi }\\
{x + \frac{\pi }{6} = \pi + \frac{\pi }{6} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{3} + 2k\pi }\\
{x = \pi + 2k\pi }
\end{array}} \right.
, $k \in Z.$

Vậy với $m = – 1$ phương trình có hai họ nghiệm.

b. Số nghiệm của phương trình bằng số giao điểm của đường thẳng $y = m$ với phần đồ thị hàm số $y = \sqrt 3 \sin x + \cos x$ trên $D = \left( { – \frac{\pi }{6},2\pi } \right].$

Xét hàm số: $y = \sqrt 3 \sin x + \cos x.$

Miền xác định: $D = \left( { – \frac{\pi }{6},2\pi } \right].$

Đạo hàm:

$y’ = \sqrt 3 \cos x – \sin x.$

$y’ = 0$ $\Leftrightarrow \sqrt 3 \cos x – \sin x = 0$ $\Leftrightarrow \cos \left( {x + \frac{\pi }{6}} \right) = 0$
\mathop \Leftrightarrow \limits^{x \in D} \left[ {\begin{array}{l}
{x = \pi /3}\\
{x = 4\pi /3}
\end{array}} \right..
Bảng biến thiên:

<img link="data_for_rag/toan11/images/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx-1.png" alt="">

Kết luận:

+ Với $|m|>2$, phương trình vô nghiệm.

+ Với $m = \pm 2$, phương trình có $1$ nghiệm thuộc $D.$

+ Với $– 2 < m \le 0$ hoặc $1 < m < 2$, phương trình có $2$ nghiệm thuộc $D.$

+ Với $0 < m \le 1$, phương trình có $3$ nghiệm thuộc $D.$

<!-- chunk:15 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 14: Biện luận theo $m$ số nghiệm thuộc $\left[ {0,\frac{{3\pi }}{2}} \right]$ của phương trình: $m\sin x + \cos x = 2m$ $(1).$

Biến đổi phương trình về dạng:

$\cos x = m(2 – \sin x)$ $\Leftrightarrow \frac{{\cos x}}{{2 – \sin x}} = m.$

Số nghiệm của phương trình bằng số giao điểm của đường thẳng $y = m$ với đồ thị hàm số $y = \frac{{\cos x}}{{2 – \sin x}}$ trên $D = \left[ {0,\frac{{3\pi }}{2}} \right].$

Xét hàm số: $y = \frac{{\cos x}}{{2 – \sin x}}.$

Miền xác định: $D = \left[ {0,\frac{{3\pi }}{2}} \right].$

Đạo hàm:

$y’ = \frac{{ – \sin x(2 – \sin x) + \cos x\cos x}}{{{{(2 – \sin x)}^2}}}$ $= \frac{{1 – 2\sin x}}{{{{(2 – \sin x)}^2}}}.$

$y’ = 0$ $\Leftrightarrow 1 – 2\sin x = 0$ $\Leftrightarrow \sin x = \frac{1}{2}$
\mathop \Leftrightarrow \limits^{x \in D} \left[ {\begin{array}{l}
{x = \pi /6}\\
{x = 5\pi /6}
\end{array}} \right..
Bảng biến thiên:

<img link="data_for_rag/toan11/images/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx-2.png" alt="">

Kết luận:

+ Với $|m| > \frac{1}{{\sqrt 3 }}$, phương trình vô nghiệm.

+ Với $m = \pm \frac{1}{{\sqrt 3 }}$ hoặc $0 < m < \frac{1}{2}$, phương trình có $1$ nghiệm thuộc $D.$

+ Với $– \frac{1}{{\sqrt 3 }} < m \le 0$ hoặc $\frac{1}{2} \le m < \frac{1}{{\sqrt 3 }}$, phương trình có $2$ nghiệm thuộc $D.$

<!-- chunk:16 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Ví dụ 15: Cho phương trình: $\sqrt 3 \sin x + m\cos x = 1.$

Tìm $m$ để phương trình có hai nghiệm ${x_1},{x_2} \in [0,2\pi )$ sao cho ${x_1} + {x_2} = \frac{{2\pi }}{3}.$

Điều kiện cần: Giả sử phương trình có nghiệm $x = \alpha \in \left[ {0,\frac{{2\pi }}{3}} \right]$, khi đó $x = \frac{{2\pi }}{3} – \alpha$ cũng là nghiệm, như vậy:
\left\{ {\begin{array}{l}
{\sqrt 3 \sin \alpha + m\cos \alpha = 1}\\
{\sqrt 3 \sin \left( {\frac{{2\pi }}{3} – \alpha } \right) + m\cos \left( {\frac{{2\pi }}{3} – \alpha } \right) = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m\cos \alpha = 1 – \sqrt 3 \sin \alpha }\\
{m\left( { – \frac{1}{2}\cos \alpha + \frac{{\sqrt 3 }}{2}\sin \alpha } \right) = 1 – \sqrt 3 \left( {\frac{{\sqrt 3 }}{2}\cos \alpha + \frac{1}{2}\sin \alpha } \right)}
\end{array}} \right..
$\Rightarrow \frac{{\cos \alpha }}{{ – \cos \alpha + \sqrt 3 \sin \alpha }}$ $= \frac{{1 – \sqrt 3 \sin \alpha }}{{2 – 3\cos \alpha – \sqrt 3 \sin \alpha }}.$

$\Leftrightarrow (2 – 3\cos \alpha – \sqrt 3 \sin \alpha )\cos \alpha$ $= ( – \cos \alpha + \sqrt 3 \sin \alpha )(1 – \sqrt 3 \sin \alpha ).$

$\Leftrightarrow 3\cos 2\alpha + \sqrt 3 \sin 2\alpha$ $= 3\cos \alpha – \sqrt 3 \sin \alpha .$

$\Leftrightarrow \frac{{\sqrt 3 }}{2}\cos 2\alpha + \frac{1}{2}\sin 2\alpha$ $= \frac{{\sqrt 3 }}{2}\cos \alpha – \frac{1}{2}\sin \alpha .$

$\Leftrightarrow \cos 2\alpha \cos \frac{\pi }{6} + \sin 2\alpha \sin \frac{\pi }{6}$ $= \cos \alpha \cos \frac{\pi }{6} – \sin \alpha \cos \frac{\pi }{6}.$

$\Leftrightarrow \cos \left( {2\alpha – \frac{\pi }{6}} \right) = \cos \left( {\alpha + \frac{\pi }{6}} \right).$
\Leftrightarrow \left[ {\begin{array}{l}
{2\alpha – \frac{\pi }{6} = \alpha + \frac{\pi }{6} + 2k\pi }\\
{2\alpha – \frac{\pi }{6} = – \alpha – \frac{\pi }{6} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\alpha = \frac{\pi }{3} + 2k\pi }\\
{\alpha = \frac{{2k\pi }}{3}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\alpha = \frac{\pi }{3}}\\
{\alpha = 0}\\
{\alpha = \frac{{2\pi }}{3}}
\end{array}} \right..
+ Với $\alpha = \frac{\pi }{3}$, thay vào phương trình ta được:

$\sqrt 3 \sin \frac{\pi }{3} + m\cos \frac{\pi }{3} = 1$ $\Leftrightarrow m = – 1.$

+ Với $\alpha = 0$, thay vào phương trình ta được:

$\sqrt 3 \sin 0 + m\cos 0 = 1$ $\Leftrightarrow m = 1.$

+ Với $\alpha = \frac{{2\pi }}{3}$, thay vào phương trình ta được:

$\sqrt 3 \sin \frac{{2\pi }}{3} + m\cos \frac{{2\pi }}{3} = 1$ $\Leftrightarrow m = 1.$

Vậy với $m = \pm 1$ là điều kiện cần.

Điều kiện đủ:

+ Với $m = 1$, thay vào phương trình ta được:

$\sqrt 3 \sin x + \cos x = 1$ $\Leftrightarrow \frac{{\sqrt 3 }}{2}\sin x + \frac{1}{2}\cos x = \frac{1}{2}$ $\Leftrightarrow \sin \left( {x + \frac{\pi }{6}} \right) = \sin \frac{\pi }{6}.$
\Leftrightarrow \left[ {\begin{array}{l}
{x + \frac{\pi }{6} = \frac{\pi }{6} + 2k\pi }\\
{x + \frac{\pi }{6} = \pi – \frac{\pi }{6} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 2k\pi }\\
{x = \frac{{2\pi }}{3} + 2k\pi }
\end{array}} \right.
$$
 
$$
\mathop \Leftrightarrow \limits^{x \in \left[ {0,2\pi } \right)} \left[ {\begin{array}{l}
{{x_1} = 0}\\
{{x_2} = \frac{{2\pi }}{3}}
\end{array}} \right..
Nhận xét rằng khi đó ${x_1} + {x_2} = \frac{{2\pi }}{3}$, do đó $m = 1$ thoả mãn.

+ Với $m = -1$: Bạn đọc tự làm tương tự.

<!-- chunk:17 level:1 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## II. CÁC BÀI TOÁN THI

## Bài 1: (ĐHMĐC – 1995): Giải phương trình: $3\sin 3x – \sqrt 3 \cos 9x = 1 + 4{\sin ^3}3x.$

Biến đổi phương trình về dạng:

$3\sin 3x – 4{\sin ^3}3x – \sqrt 3 \cos 9x = 1$ $\Leftrightarrow \sin 9x – \sqrt 3 \cos 9x = 1.$

Bạn đọc tự giải tiếp.

## Bài 2. (ĐHMTCN – 1996): Giải phương trình:

$\cos 7x\cos 5x – \sqrt 3 \sin 2x$ $= 1 – \sin 7x\sin 5x.$

Biến đổi phương trình về dạng:

$\cos 7x\cos 5x + \sin 7x\sin 5x$ $– \sqrt 3 \sin 2x = 1$ $\Leftrightarrow \cos 2x – \sqrt 3 \sin 2x = 1.$

Bạn đọc tự giải tiếp.

## Bài 3: (ĐHKTQD – 1997): Tìm các nghiệm thuộc khoảng $\left( {\frac{{2\pi }}{5},\frac{{6\pi }}{7}} \right)$ của phương trình: $\sqrt 3 \sin 7x – \cos 7x = \sqrt 2 .$

Biến đổi phương trình về dạng:

$\Leftrightarrow \frac{{\sqrt 3 }}{2}\sin 7x – \frac{1}{2}\cos 7x = \frac{{\sqrt 2 }}{2}$ $\Leftrightarrow \sin 7x\cos \frac{\pi }{6} – \cos 7x\sin \frac{\pi }{6} = \frac{{\sqrt 2 }}{2}.$

$\Leftrightarrow \sin \left( {7x – \frac{\pi }{6}} \right) = \sin \frac{\pi }{4}$
\Leftrightarrow \left[ {\begin{array}{l}
{7x – \frac{\pi }{6} = \frac{\pi }{4} + 2k\pi }\\
{7x – \frac{\pi }{6} = \pi – \frac{\pi }{4} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{{5\pi }}{{84}} + \frac{{2k\pi }}{7}}\\
{x = \frac{{11\pi }}{{84}} + \frac{{2k\pi }}{7}}
\end{array}} \right.
, $k \in Z.$

+ Với họ nghiệm $x = \frac{{5\pi }}{{84}} + \frac{{2k\pi }}{7}$, ta được:

$\frac{{2\pi }}{5} < \frac{{5\pi }}{{84}} + \frac{{2k\pi }}{7} < \frac{{6\pi }}{7}$ $\Leftrightarrow \frac{2}{5} – \frac{5}{{84}} < \frac{{2k}}{7} < \frac{6}{7} – \frac{5}{{84}}$ $\Rightarrow k = 2.$

Khi đó ta được nghiệm: ${x_1} = \frac{{5\pi }}{{84}} + \frac{{4\pi }}{7} = \frac{{53\pi }}{{84}}.$

+ Với họ nghiệm $x = \frac{{11\pi }}{{84}} + \frac{{2k\pi }}{7}$, ta được:

$\frac{{2\pi }}{5} < \frac{{11\pi }}{{84}} + \frac{{2k\pi }}{7} < \frac{{6\pi }}{7}$ $\Leftrightarrow \frac{2}{5} – \frac{{11}}{{84}} < \frac{{2k}}{7} < \frac{6}{7} – \frac{{11}}{{84}}$ $\Rightarrow k = 1,2.$

Khi đó ta được nghiệm: ${x_2} = \frac{{11\pi }}{{84}} + \frac{{2\pi }}{7} = \frac{{35\pi }}{{84}}$ và ${x_3} = \frac{{11\pi }}{{84}} + \frac{{4\pi }}{7} = \frac{{59\pi }}{{84}}.$

## Bài 4: Cho phương trình:

a. Giải phương trình với $m = \sqrt 3 .$

b. Tìm $m$ để phương trình có $4$ nghiệm phân biệt thuộc $\left( { – \pi ,\frac{{7\pi }}{3}} \right).$

a. Bạn đọc tự giải.

b. Biến đổi phương trình về dạng:

$\sin x = m(1 – \cos x)$
\Leftrightarrow \left[ {\begin{array}{c}
{\cos x = 1}\\
{\frac{{\sin x}}{{1 – \cos x}} = m}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0 \vee x = 2\pi }\\
{\frac{{\sin x}}{{1 – \cos x}} = m\:(*)}
\end{array}} \right..
Vậy để phương trình ban đầu có $4$ nghiệm phân biệt thuộc $\left( { – \pi ,\frac{{7\pi }}{3}} \right)$ điều kiện là phương trình $(*)$ có $2$ nghiệm phân biệt thuộc $\left( { – \pi ,\frac{{7\pi }}{3}} \right).$

Số nghiệm của phương trình $(*)$ bằng số giao điểm của đường thẳng $y = m$ với đồ thị hàm số $y = \frac{{\sin x}}{{1 – \cos x}}$ trên $D = \left( { – \pi ,\frac{{7\pi }}{3}} \right).$

Xét hàm số $y = \frac{{\sin x}}{{1 – \cos x}}.$

Miền xác định $D = \left( { – \pi ,\frac{{7\pi }}{3}} \right).$

Đạo hàm $y’ = \frac{{\cos x – 1}}{{{{(1 – \cos x)}^2}}} \le 0$, $\forall x \in D.$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx-3.png" alt="">

Khi đó với $m \le 0 \vee m \ge \sqrt 3$ phương trình $(*)$ có $2$ nghiệm phân biệt thuộc khoảng $\left( { – \pi ,\frac{{7\pi }}{3}} \right).$

## Bài 5: (ĐHTCKT TPHCM – 1995): Cho phương trình: $m\sin x + (m + 1)\cos x + 1 = 0.$

Tìm $m$ để phương trình có hai nghiệm ${x_1},{x_2} \in [0,2\pi ]$ và hai nghiệm này cách nhau $\frac{\pi }{2}.$

Điều kiện cần: Giả sử phương trình có nghiệm $x = \alpha \in \left[ {0,\frac{{3\pi }}{2}} \right]$, khi đó $x = \alpha + \frac{\pi }{2}$ cũng là nghiệm, như vậy:
\left\{ {\begin{array}{l}
{m\sin \alpha + (m + 1)\cos \alpha + 1 = 0}\\
{m\sin \left( {\alpha + \frac{\pi }{2}} \right) + (m + 1)\cos \left( {\alpha + \frac{\pi }{2}} \right) + 1 = 0}
\end{array}} \right..

\Leftrightarrow \left\{ {\begin{array}{l}
{m\sin \alpha + (m + 1)\cos \alpha + 1 = 0}\\
{m\cos \alpha – (m + 1)\sin \alpha + 1 = 0}
\end{array}} \right..

\Leftrightarrow \left\{ {\begin{array}{l}
{m(\sin \alpha + \cos \alpha ) = – 1 – \cos \alpha }\\
{m(\cos \alpha – \sin \alpha ) = \sin \alpha – 1}
\end{array}} \right..
$$

$\Rightarrow \frac{{\sin \alpha + \cos \alpha }}{{\cos \alpha – \sin \alpha }} = \frac{{1 + \cos \alpha }}{{1 – \sin \alpha }}.$

$\Leftrightarrow (\sin \alpha + \cos \alpha )(1 – \sin \alpha )$ $= (\cos \alpha – \sin \alpha )(1 + \cos \alpha )$ $\Leftrightarrow \sin \alpha = \frac{1}{2}$ $\Leftrightarrow \alpha = \frac{\pi }{6}$ hoặc $\alpha = \frac{{5\pi }}{6}.$

+ Với $\alpha = \frac{\pi }{6}$, thay vào phương trình ta được:

$m\sin \frac{\pi }{6} + (m + 1)\cos \frac{\pi }{6} + 1 = 0$ $\Leftrightarrow m = – \frac{{1 + \sqrt 3 }}{2}.$

+ Với $\alpha = \frac{{5\pi }}{6}$, thay vào phương trình ta được:

$m\sin \frac{{5\pi }}{6} + (m + 1)\cos \frac{{5\pi }}{6} + 1 = 0$ $\Leftrightarrow m = – \frac{{1 – \sqrt 3 }}{2}.$

Vậy với $m = – \frac{{1 \pm \sqrt 3 }}{2}$ là điều kiện cần.

Điều kiện đủ: Bạn đọc tự giải.

<!-- chunk:18 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Bài tập 1: Giải các phương trình sau:

a. ${\cos ^2}x – \sqrt 3 \sin 2x = {\sin ^3}x + 1.$

b. $3\sin x – \sqrt 3 \cos 3x = 4{\sin ^3}x – 1.$

<!-- chunk:19 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Bài tập 2: Giải các phương trình sau:

a. $2\cos x(\sin x – 1) = \sqrt 3 \cos 2x.$

b. $2\sin 3x – \sin 2x + \sqrt 3 \cos 2x = 0.$

<!-- chunk:20 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Bài tập 3: Giải các phương trình sau:

a. $3\sin 2x + 4\cos 2x + 5\cos 2003x = 0.$

b. $\sqrt 3 \sin 4x – \cos 4x = \sin x – \sqrt 3 \cos x.$

<!-- chunk:21 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Bài tập 4: Giải các phương trình sau:

a. $\sqrt 3 \sin \left( {x – \frac{\pi }{3}} \right) + \sin \left( {x + \frac{\pi }{6}} \right)$ $– 2\sin 1972x = 0.$

b. $\sin x = \frac{1}{3}(3 – \sqrt 3 \cos x).$

<!-- chunk:22 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Bài tập 5: Giải các phương trình sau:

a. $\sin 2x + (\sqrt 3 – 2)\cos 2x = 1.$

b. $(1 – \sqrt 3 )\sin x + (1 + \sqrt 3 )\cos x = 2.$

<!-- chunk:23 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Bài tập 6: Giải các phương trình sau:

a. $3\cos x – \sin 2x = \sqrt 3 (\cos 2x + \sin x).$

b. $\sqrt 2 \cos \left( {\frac{x}{5} – \frac{\pi }{{12}}} \right) – \sqrt 6 \sin \left( {\frac{x}{5} – \frac{\pi }{{12}}} \right)$ $= 2\sin \left( {\frac{x}{5} + \frac{{2\pi }}{3}} \right) – 2\sin \left( {\frac{{3x}}{5} + \frac{\pi }{6}} \right).$

<!-- chunk:24 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Bài tập 7: Cho phương trình: $(m – 1)\sin x – \cos x = 1.$

a. Giải phương trình với $m = 1.$

b. Tìm $m$ để phương trình có nghiệm thuộc $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$

<!-- chunk:25 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Bài tập 8: Cho phương trình: $m\sin x + 2\cos x = 1 – m.$

a. Giải phương trình với $m = 2\sqrt 3 .$

b. Tìm $m$ để phương trình có nghiệm thuộc $\left[ { – \frac{\pi }{2},\frac{\pi }{2}} \right].$

<!-- chunk:26 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Bài tập 9: Cho phương trình: $\sqrt 3 \sin x – \cos x = m.$

a. Giải phương trình với $m = 1.$

b. Biện luận theo $m$ số nghiệm thuộc $\left( { – \frac{{5\pi }}{6},3\pi } \right]$ của phương trình.

<!-- chunk:27 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-nhat-doi-voi-sinx-va-cosx.html -->
## Bài tập 11: Giải và biện luận theo $m$ phương trình:

$\frac{{a – b\cos x}}{{\sin x}} = \frac{{2\sqrt {{a^2} – {b^2}} \tan y}}{{1 + {{\tan }^2}y}}.$