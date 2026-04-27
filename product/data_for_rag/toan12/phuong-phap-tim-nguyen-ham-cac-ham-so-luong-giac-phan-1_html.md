# Phương pháp tìm nguyên hàm các hàm số lượng giác (Phần 1)

<!-- chunk:0 level:0 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
Bài viết trình bày phương pháp tìm nguyên hàm các hàm số lượng giác, đây là dạng nguyên hàm thường gặp trong các đề thi THPT Quốc gia, đề tuyển sinh Đại học – Cao đẳng.

Phương pháp 1: Xác định nguyên hàm các hàm số lượng giác bằng cách sử dụng các dạng nguyên hàm cơ bản.

<!-- chunk:1 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Dạng 1: Tìm nguyên hàm $I = \int {\frac{{dx}}{{\sin \left( {x + a} \right)\sin \left( {x + b} \right)}}} .$
Cách giải: Ta thực hiện theo các bước sau:

+ Bước 1: Sử dụng đồng nhất thức: $1 = \frac{{\sin \left( {a – b} \right)}}{{\sin \left( {a – b} \right)}}$ $= \frac{{\sin \left[ {\left( {x + a} \right) – \left( {x + b} \right)} \right]}}{{\sin \left( {a – b} \right)}}.$

+ Bước 2: Biến đổi: $I = \int {\frac{{dx}}{{\sin \left( {x + a} \right)\sin \left( {x + b} \right)}}}$ $= \frac{1}{{\sin \left( {a – b} \right)}}\int {\frac{{\sin \left[ {\left( {x + a} \right) – \left( {x + b} \right)} \right]}}{{\sin \left( {x + a} \right)\sin \left( {x + b} \right)}}dx}$ $= \frac{1}{{\sin \left( {a – b} \right)}}\int {\frac{{\sin \left( {x + a} \right)\cos \left( {x + b} \right) – \cos \left( {x + a} \right)\sin \left( {x + b} \right)}}{{\sin \left( {x + a} \right)\sin \left( {x + b} \right)}}dx}$ $= \frac{1}{{\sin \left( {a – b} \right)}}\left[ {\int {\frac{{\cos \left( {x + b} \right)}}{{\sin \left( {x + b} \right)}}dx} – \int {\frac{{\cos \left( {x + a} \right)}}{{\sin \left( {x + a} \right)}}dx} } \right]$ $= \frac{1}{{\sin \left( {a – b} \right)}}\left[ {\ln \left| {\sin \left( {x + b} \right)} \right| – \ln \left| {\sin \left( {x + a} \right)} \right|} \right] + C$ $= \frac{1}{{\sin \left( {a – b} \right)}}\ln \left| {\frac{{\sin \left( {x + b} \right)}}{{\sin \left( {x + a} \right)}}} \right| + C.$

Chú ý: Phương pháp trên cũng được được áp dụng cho các dạng nguyên hàm sau:

+ Nguyên hàm $I = \int {\frac{{dx}}{{\cos \left( {x + a} \right)\cos \left( {x + b} \right)}}}$ bằng cách sử dụng đồng nhất thức $1 = \frac{{\sin \left( {a – b} \right)}}{{\sin \left( {a – b} \right)}}$ $= \frac{{\sin \left[ {\left( {x + a} \right) – \left( {x + b} \right)} \right]}}{{\sin \left( {a – b} \right)}}.$

+ Nguyên hàm $I = \int {\frac{{dx}}{{\sin \left( {x + a} \right)\cos \left( {x + b} \right)}}}$ bằng cách sử dụng đồng nhất thức $1 = \frac{{\cos \left( {a – b} \right)}}{{\cos \left( {a – b} \right)}}$ $= \frac{{\cos \left[ {\left( {x + a} \right) – \left( {x + b} \right)} \right]}}{{\cos \left( {a – b} \right)}}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Ví dụ 1: Tìm họ nguyên hàm của hàm số: $f\left( x \right) = \frac{1}{{\sin x.\cos \left( {x + \frac{\pi }{4}} \right)}}.$

Cách 1: Sử dụng đồng nhất thức: $1 = \frac{{\cos \frac{\pi }{4}}}{{\cos \frac{\pi }{4}}}$ $= \frac{{\cos \left[ {\left( {x + \frac{\pi }{4}} \right) – x} \right]}}{{\frac{{\sqrt 2 }}{2}}}$ $= \sqrt 2 \cos \left[ {\left( {x + \frac{\pi }{4}} \right) – x} \right].$

Ta được: $F\left( x \right) = \sqrt 2 \int {\frac{{\cos \left[ {\left( {x + \frac{\pi }{4}} \right) – x} \right]}}{{\sin x.\cos \left( {x + \frac{\pi }{4}} \right)}}}$ $= \sqrt 2 \int {\frac{{\cos \left( {x + \frac{\pi }{4}} \right)\cos x + \sin \left( {x + \frac{\pi }{4}} \right)\sin x}}{{\sin x.\cos \left( {x + \frac{\pi }{4}} \right)}}dx}$ $= \sqrt 2 \left[ {\int {\frac{{\cos x}}{{\sin x}}dx} + \int {\frac{{\sin \left( {x + \frac{\pi }{4}} \right)}}{{\cos \left( {x + \frac{\pi }{4}} \right)}}dx} } \right]$ $= \sqrt 2 \left[ {\ln \left| {\sin x} \right| – \ln \left| {\cos \left( {x + \frac{\pi }{4}} \right)} \right|} \right] + C.$

Cách 2: Ta có:

$F\left( x \right) = \sqrt 2 \int {\frac{{dx}}{{\sin x\left( {\cos x – \sin x} \right)}}}$ $= \sqrt 2 \int {\frac{{dx}}{{{{\sin }^2}x\left( {\cot x – 1} \right)}}}$ $= – \sqrt 2 \int {\frac{{d\left( {\cot x} \right)}}{{\cot x – 1}}}$ $= – \sqrt 2 \int {\frac{{d\left( {\cot x – 1} \right)}}{{\cot x – 1}}}$ $= – \sqrt 2 \ln \left| {\cot x – 1} \right| + C.$

<!-- chunk:3 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Dạng 2: Tìm nguyên hàm $I = \int {\frac{{dx}}{{\sin x + \sin \alpha }}} .$

Cách giải: Ta thực hiện theo các bước sau:

+ Bước 1: Biến đổi $I$ về dạng: $I = \int {\frac{{dx}}{{\sin x + \sin \alpha }}}$ $= \frac{1}{2}\int {\frac{{dx}}{{\sin \frac{{x + \alpha }}{2}\cos \frac{{x – \alpha }}{2}}}} .$

+ Bước 2: Áp dụng dạng 1 đã trình bày ở phần trên để tìm nguyên hàm này.

Chú ý: Phương pháp trên cũng được được áp dụng cho các dạng nguyên hàm sau:

+ Nguyên hàm $I = \int {\frac{{dx}}{{\sin x + m}}}$, với $\left| m \right| \le 1.$

+ Nguyên hàm $I = \int {\frac{{dx}}{{\cos x + \cos \alpha }}}$ và $I = \int {\frac{{dx}}{{\cos x + m}}}$ với $\left| m \right| \le 1.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Ví dụ 2: Tìm họ nguyên hàm của hàm số: $f\left( x \right) = \frac{1}{{2\sin x + 1}}.$

Biến đổi $f\left( x \right)$ về dạng: $f\left( x \right) = \frac{1}{{2\left( {\sin x + \frac{1}{2}} \right)}}$ $= \frac{1}{2}.\frac{1}{{\sin x + \sin \frac{\pi }{6}}}$ $= \frac{1}{4}.\frac{1}{{\sin \frac{{6x + \pi }}{{12}}.\cos \frac{{6x – \pi }}{{12}}}}.$

Sử dụng đồng nhất thức: $1 = \frac{{\cos \frac{\pi }{6}}}{{\cos \frac{\pi }{6}}}$ $= \frac{{\cos \left( {\frac{{6x + \pi }}{{12}} – \frac{{6x – \pi }}{{12}}} \right)}}{{\frac{{\sqrt 3 }}{2}}}$ $= \frac{2}{{\sqrt 3 }}\cos \left( {\frac{{6x + \pi }}{{12}} – \frac{{6x – \pi }}{{12}}} \right).$

Ta được: $F\left( x \right) = \frac{1}{{2\sqrt 3 }}\int {\frac{{\cos \left( {\frac{{6x + \pi }}{{12}} – \frac{{6x – \pi }}{{12}}} \right)}}{{\sin \frac{{6x + \pi }}{{12}}.\cos \frac{{6x – \pi }}{{12}}}}dx}$ $= \frac{1}{{2\sqrt 3 }}\int {\frac{{\cos \frac{{6x + \pi }}{{12}}.\cos \frac{{6x – \pi }}{{12}} + \sin \frac{{6x + \pi }}{{12}}\sin \frac{{6x – \pi }}{{12}}}}{{\sin \frac{{6x + \pi }}{{12}}.\cos \frac{{6x – \pi }}{{12}}}}dx}$ $= \frac{1}{{2\sqrt 3 }}\left[ {\int {\frac{{\cos \frac{{6x + \pi }}{{12}}}}{{\sin \frac{{6x + \pi }}{{12}}}}dx} + \int {\frac{{\sin \frac{{6x – \pi }}{{12}}}}{{\cos \frac{{6x – \pi }}{{12}}}}dx} } \right]$ $= \frac{1}{{2\sqrt 3 }}\left[ {\ln \left| {\sin \frac{{6x + \pi }}{{12}}} \right| – \ln \left| {\cos \frac{{6x – \pi }}{{12}}} \right|} \right] + C$ $= \frac{1}{{2\sqrt 3 }}\ln \left| {\frac{{\sin \frac{{6x + \pi }}{{12}}}}{{\cos \frac{{6x – \pi }}{{12}}}}} \right| + C.$

<!-- chunk:5 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Dạng 3: Tìm nguyên hàm: $I = \int {\tan x.\tan \left( {x + \alpha } \right)dx} .$
Cách giải: Ta thực hiện theo các bước sau:

+ Bước 1: Biến đổi $I$ về dạng: $I = \int {\tan x.\tan \left( {x + \alpha } \right)dx}$ $= \int {\frac{{\sin x.\sin \left( {x + \alpha } \right)}}{{\cos x.\cos \left( {x + \alpha } \right)}}dx}$ $= \int {\left( {\frac{{\cos x.\cos \left( {x + \alpha } \right) + \sin x.\sin \left( {x + \alpha } \right)}}{{\cos x.\cos \left( {x + \alpha } \right)}} – 1} \right)dx}$ $= \int {\frac{{\cos \alpha dx}}{{\cos x.\cos \left( {x + \alpha } \right)}}} – \int {dx}$ $= \cos \alpha \int {\frac{{dx}}{{\cos x.\cos \left( {x + \alpha } \right)}} – x.}$

+ Bước 2: Áp dụng dạng 1 đã trình bày ở phần trên để giải tiếp.

Chú ý: Phương pháp trên cũng được được áp dụng cho các dạng nguyên hàm sau:

+ Nguyên hàm $I = \int {\tan \left( {x + \alpha } \right).\cot \left( {x + \beta } \right)dx} .$

+ Nguyên hàm $I = \int {\cot \left( {x + \alpha } \right).\cot \left( {x + \beta } \right)dx} .$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Ví dụ 3: Tìm họ nguyên hàm của hàm số: $f\left( x \right) = \tan x.\tan \left( {x + \frac{\pi }{4}} \right).$

Biến đổi $f\left( x \right)$ về dạng: $f\left( x \right) = \frac{{\sin x.\sin \left( {x + \frac{\pi }{4}} \right)}}{{\cos x.\cos \left( {x + \frac{\pi }{4}} \right)}}$ $= \frac{{\cos x.\cos \left( {x + \frac{\pi }{4}} \right) + \sin x.\sin \left( {x + \frac{\pi }{4}} \right)}}{{\cos x.\cos \left( {x + \frac{\pi }{4}} \right)}} – 1$ $= \frac{{\cos \frac{\pi }{4}}}{{\cos x.\cos \left( {x + \frac{\pi }{4}} \right)}} – 1$ $= \frac{{\sqrt 2 }}{2}.\frac{1}{{\cos x.\cos \left( {x + \frac{\pi }{4}} \right)}} – 1.$

Khi đó: $F\left( x \right) = \frac{{\sqrt 2 }}{2}\int {\frac{{dx}}{{\cos x.\cos \left( {x + \frac{\pi }{4}} \right)}}} – \int {dx}$ $= – x + \frac{{\sqrt 2 }}{2}\int {\frac{{dx}}{{\cos x.\cos \left( {x + \frac{\pi }{4}} \right)}}.}$

Để xác định nguyên hàm $J = \frac{{dx}}{{\cos x.\cos \left( {x + \frac{\pi }{4}} \right)}}$ ta lựa chọn một trong hai cách sau:

Cách 1: Sử dụng đồng nhất thức: $1 = \frac{{\sin \frac{\pi }{4}}}{{\sin \frac{\pi }{4}}} = \frac{{\sin \left[ {\left( {x + \frac{\pi }{4}} \right) – x} \right]}}{{\frac{{\sqrt 2 }}{2}}}$ $= \sqrt 2 \sin \left[ {\left( {x + \frac{\pi }{4}} \right) – x} \right].$

Ta được: $J = \sqrt 2 \int {\frac{{\sin \left[ {\left( {x + \frac{\pi }{4}} \right) – x} \right]}}{{\cos x.\cos \left( {x + \frac{\pi }{4}} \right)}}dx}$ $= \sqrt 2 \int {\frac{{\sin \left( {x + \frac{\pi }{4}} \right)\cos x – \cos \left( {x + \frac{\pi }{4}} \right)\sin x}}{{\cos x.\cos \left( {x + \frac{\pi }{4}} \right)}}dx}$ $= \sqrt 2 \left[ {\int {\frac{{\sin \left( {x + \frac{\pi }{4}} \right)}}{{\cos \left( {x + \frac{\pi }{4}} \right)}}dx} – \int {\frac{{\sin x}}{{\cos x}}dx} } \right]$ $= \sqrt 2 \left[ { – \ln \left| {\cos \left( {x + \frac{\pi }{4}} \right)} \right| + \ln \left| {\cos x} \right|} \right] + C$ $= \sqrt 2 \ln \left| {\frac{{\cos x}}{{\cos \left( {x + \frac{\pi }{4}} \right)}}} \right| + C$ $= – \sqrt 2 \ln \left| {1 – \tan x} \right| + C.$

Cách 2: Ta có: $J = \sqrt 2 \int {\frac{{dx}}{{\cos x\left( {\cos x – \sin x} \right)}}}$ $= \sqrt 2 \int {\frac{{dx}}{{{{\cos }^2}x\left( {1 – \tan x} \right)}}}$ $= \sqrt 2 \int {\frac{{d\left( {\tan x} \right)}}{{1 – \tan x}}}$ $= – \sqrt 2 \int {\frac{{d(1 – \tan x)}}{{1 – \tan x}}}$ $= – \sqrt 2 \ln \left| {1 – \tan x} \right| + C.$

Vậy ta được: $F\left( x \right) = – x – \ln \left| {1 – \tan x} \right| + C.$

<!-- chunk:7 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Dạng 4: Tìm nguyên hàm: $I = \int {\frac{{dx}}{{a\sin x + b\cos x}}} .$
Cách giải: Ta có thể lựa chọn hai cách biến đổi:

Cách 1: Ta có: $I = \frac{1}{{\sqrt {{a^2} + {b^2}} }}\int {\frac{{dx}}{{\sin (x + \alpha )}}}$ $= \frac{1}{{\sqrt {{a^2} + {b^2}} }}\int {\frac{{dx}}{{2\sin \frac{{x + \alpha }}{2}\cos \frac{{x + \alpha }}{2}}}}$ $= \frac{1}{{\sqrt {{a^2} + {b^2}} }}\int {\frac{{dx}}{{2\tan \frac{{x + \alpha }}{2}{{\cos }^2}\frac{{x + \alpha }}{2}}}}$ $= \frac{1}{{\sqrt {{a^2} + {b^2}} }}\int {\frac{{d\left( {\tan \frac{{x + \alpha }}{2}} \right)}}{{\tan \frac{{x + \alpha }}{2}}}}$ $= \frac{1}{{\sqrt {{a^2} + {b^2}} }}\ln \left| {\tan \frac{{x + \alpha }}{2}} \right| + C.$

Cách 2: Ta có: $I = \frac{1}{{\sqrt {{a^2} + {b^2}} }}\int {\frac{{dx}}{{\sin (x + \alpha )}}}$ $= \frac{1}{{\sqrt {{a^2} + {b^2}} }}\int {\frac{{\sin (x + \alpha )dx}}{{{{\sin }^2}(x + \alpha )}}}$ $= – \frac{1}{{\sqrt {{a^2} + {b^2}} }}\int {\frac{{d\left[ {\cos (x + \alpha )} \right]}}{{{{\cos }^2}(x + \alpha ) – 1}}}$ $= – \frac{1}{{2\sqrt {{a^2} + {b^2}} }}\ln \left| {\frac{{\cos (x + \alpha ) – 1}}{{\cos (x + \alpha ) + 1}}} \right| + C.$

Chú ý: Chúng ta cũng có thể thực hiện bằng phương pháp đại số hóa với việc đổi biến: $t = \tan \frac{x}{2}.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Ví dụ 4: Tìm họ nguyên hàm của hàm số: $f(x) = \frac{2}{{\sqrt 3 \sin x + \cos x}}.$

Ta có: $F(x) = \int {\frac{{2dx}}{{\sqrt 3 \sin x + \cos x}}}$ $=\int {\frac{{dx}}{{\sin \left( {x + \frac{\pi }{6}} \right)}}}$ $= \int {\frac{{{\rm{d}}x}}{{2\sin \left( {\frac{x}{2} + \frac{\pi }{{12}}} \right)\cos \left( {\frac{x}{2} + \frac{\pi }{{12}}} \right)}}}$ $= \int {\frac{{{\rm{d}}x}}{{ 2\tan \left( {\frac{x}{2} + \frac{\pi }{{12}}} \right){{\cos }^2}\left( {\frac{x}{2} + \frac{\pi }{{12}}} \right)}}}$ $= \int {\frac{{d\left[ {\tan \left( {\frac{x}{2} + \frac{\pi }{{12}}} \right)} \right]}}{{\tan \left( {\frac{x}{2} + \frac{\pi }{{12}}} \right)}}}$ $= \ln \left| {\tan \left( {\frac{x}{2} + \frac{\pi }{{12}}} \right)} \right| + C.$

<!-- chunk:9 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Dạng 5: Tìm nguyên hàm: $I = \int {\frac{{{a_1}\sin x + {b_1}\cos x}}{{{a_2}\sin x + {b_2}\cos x}}} dx.$
Cách giải: Ta thực hiện theo các bước sau:

+ Bước 1: Biến đổi: ${a_1}\sin x + {b_1}\cos x$ $= A\left( {{a_2}\sin x + {b_2}\cos x} \right) + B\left( {{a_2}\cos x – {b_2}\sin x} \right).$

+ Bước 2: Khi đó: $I = \int {\frac{{A\left( {{a_2}\sin x + {b_2}\cos x} \right) + B\left( {{a_2}\cos x – {b_2}\sin x} \right)}}{{{a_2}\sin x + {b_2}\cos x}}} dx$ $= A\int {dx + B\int {\frac{{{a_2}\cos x – {b_2}\sin x}}{{{a_2}\sin x + {b_2}\cos x}}dx} }$ $= Ax + B\ln \left| {{a_2}\sin x + {b_2}\cos x} \right| + C.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Ví dụ 5: Tìm họ nguyên hàm của hàm số: $f(x) = \frac{{4\sin x + 3\cos x}}{{\sin x + 2\cos x}}.$

Biến đổi: $4\sin x + 3\cos x$ $= a(\sin x + 2\cos x) + b(\cos x – 2\sin x)$ $= (a – 2b)\sin x + (2a + b)\cos x.$

Đồng nhất đẳng thức, ta được: 
$$
\left\{ {\begin{array}{l}
{a – 2b = 4}\\
{2a + b = 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = 2}\\
{b = – 1}
\end{array}} \right.
$$

Khi đó: $f(x) = \frac{{2(\sin x + 2\cos x) – (\cos x – 2\sin x)}}{{\sin x + 2\cos x}}$ $= 2 – \frac{{\cos x – 2\sin x}}{{\sin x + 2\cos x}}.$

Do đó: $F(x) = \int {\left( {2 – \frac{{\cos x – 2\sin x}}{{\sin x + 2\cos x}}} \right)} dx$ $= 2\int {dx} – \int {\frac{{d(\sin x + 2\cos x)}}{{\sin x + 2\cos x}}}$ $= 2x – \ln |\sin x + 2\cos x| + C.$

<!-- chunk:11 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Dạng 6: Tìm nguyên hàm: $I = \int {\frac{{{a_1}\sin x + {b_1}\cos x}}{{{{\left( {{a_2}\sin x + {b_2}\cos x} \right)}^2}}}} dx.$

Cách giải: Ta thực hiện theo các bước sau:

+ Bước 1: Biến đổi: ${a_1}\sin x + {b_1}\cos x$ $= A\left( {{a_2}\sin x + {b_2}\cos x} \right) + {\rm{B}}\left( {{a_2}\cos x – {b_2}\sin x} \right).$

+ Bước 2: Khi đó: $I = \int {\frac{{A\left( {{a_2}\sin x + {b_2}\cos x} \right) + B\left( {{a_2}\cos x – {b_2}\sin x} \right)}}{{{{\left( {{a_2}\sin x + {b_2}\cos x} \right)}^2}}}} dx$ $= A\int {\frac{{dx}}{{{a_2}\sin x + {b_2}\cos x}}} + B\int {\frac{{{a_2}\cos x – {b_2}\sin x}}{{{{\left( {{a_2}\sin x + {b_2}\cos x} \right)}^2}}}} dx$ $= \frac{{\rm{A}}}{{\sqrt {{\rm{a}}_2^2 + {\rm{b}}_2^2} }}\int {\frac{{dx}}{{\sin \left( {x + \alpha } \right)}}} – \frac{{\rm{B}}}{{{{\rm{a}}_2}\sin x + {{\rm{b}}_2}\cos x}}$ $= \frac{{\rm{A}}}{{\sqrt {{\rm{a}}_2^2 + {\rm{b}}_2^2} }}\ln \left| {{\rm{tan}}\frac{{x + \alpha }}{2}} \right| – \frac{{\rm{B}}}{{{{\rm{a}}_2}\sin x + {b_2}\cos x}} + {\rm{C}}{\rm{.}}$

Trong đó: $\sin \alpha = \frac{{{{\rm{b}}_2}}}{{\sqrt {{\rm{a}}_2^2 + {\rm{b}}_2^2} }}$ và $\cos \alpha = \frac{{{{\rm{a}}_2}}}{{\sqrt {{\rm{a}}_2^2 + {\rm{b}}_2^2} }}.$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Ví dụ 6: Tìm họ nguyên hàm của hàm số: $f(x) = \frac{{8\cos x}}{{2 + \sqrt 3 \sin 2x – \cos 2x}}.$

Biến đổi: $f(x) = \frac{{8\cos x}}{{3{{\sin }^2}x + 2\sqrt 3 \sin x\cos x + {{\cos }^2}x}}$ $= \frac{{8\cos x}}{{{{\left( {\sqrt 3 \sin x + \cos x} \right)}^2}}}.$

Giả sử: $8\cos x$ $= a\left( {\sqrt 3 \sin x + \cos x} \right) + b\left( {\sqrt 3 \cos x – \sin x} \right)$ $= \left( {a\sqrt 3 – b} \right)\sin x + \left( {a + b\sqrt 3 } \right)\cos x.$

Đồng nhất đẳng thức, ta được: 
$$
\left\{ {\begin{array}{l}
{a\sqrt 3 – b = 0}\\
{a + b\sqrt 3 = 8}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = 2}\\
{b = 2\sqrt 3 }
\end{array}} \right.
$$

Khi đó: $f(x) = \frac{2}{{\sqrt 3 \sin x + \cos x}} – \frac{{2\sqrt 3 \left( {\sqrt 3 \cos x – \sin x} \right)}}{{{{\left( {\sqrt 3 \sin x + \cos x} \right)}^2}}}.$

Do đó: $F(x) = \int {\frac{{2dx}}{{\sqrt 3 \sin x + \cos x}}} – 2\sqrt 3 \int {\frac{{d\left( {\sqrt 3 \sin x + \cos x} \right)}}{{{{\left( {\sqrt 3 \sin x + \cos x} \right)}^2}}}}$ $= \frac{1}{2}\ln \left| {\tan \left( {\frac{x}{2} + \frac{\pi }{{12}}} \right)} \right| – \frac{{2\sqrt 3 }}{{\sqrt 3 \sin x + \cos x}} + C.$

Chú ý: Trong lời giải trên ta đã tận dụng kết quả trong ví dụ 4 là: $\int {\frac{{2dx}}{{\sqrt 3 \sin x + \cos x}}}$ $= \frac{1}{2}\ln \left| {\tan \left( {\frac{{\rm{x}}}{2} + \frac{\pi }{{12}}} \right)} \right| + {\rm{C}}.$

<!-- chunk:13 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Dạng 7: Tìm nguyên hàm: $I = \int {\frac{{{\rm{d}}x}}{{ asin x + b\cos x + c}}} .$

Cách giải: Ta xét 3 trường hợp sau:

+ Trường hợp 1: Nếu $c = \sqrt {{a^2} + {b^2}}$ thì ta thực hiện phép biến đổi: $\frac{1}{{ asin x + b\cos x + c}}$ $= \frac{1}{{c\left[ {1 + \cos (x – \alpha )} \right]}}$ $= \frac{1}{{2c}} \cdot \frac{1}{{{{\cos }^2}\frac{{x – \alpha }}{2}}}$, trong đó: $\sin \alpha = \frac{{\rm{a}}}{{\sqrt {{{\rm{a}}^2} + {{\rm{b}}^2}} }}$ và $\cos \alpha = \frac{b}{{\sqrt {{a^2} + {b^2}} }}.$

Khi đó: $I = \frac{1}{{2c}}\int {\frac{{dx}}{{{{\cos }^2}\frac{{x – \alpha }}{2}}}}$ $= \frac{1}{c}\int {\frac{{d\left( {\frac{{x – \alpha }}{2}} \right)}}{{{{\cos }^2}\frac{{x – \alpha }}{2}}}}$ $= \frac{1}{c}\tan \frac{{x – \alpha }}{2} + C.$

+ Trường hợp 2: Nếu $c = – \sqrt {{a^2} + {b^2}}$ thì ta thực hiện phép biến đổi: $\frac{1}{{ asin x + b\cos x + c}}$ $= \frac{1}{{c\left[ {1 – \cos (x – \alpha )} \right]}}$ $= \frac{1}{{2c}} \cdot \frac{1}{{{{\sin }^2}\frac{{x – \alpha }}{2}}}$, trong đó: $\sin \alpha = \frac{a}{{\sqrt {{a^2} + {b^2}} }}$ và $\cos \alpha = \frac{b}{{\sqrt {{a^2} + {b^2}} }}.$

Khi đó: $I = \frac{1}{{2c}}\int {\frac{{dx}}{{{{\sin }^2}\frac{{x – \alpha }}{2}}}}$ $= \frac{1}{c}\int {\frac{{d\left( {\frac{{x – \alpha }}{2}} \right)}}{{{{\sin }^2}\frac{{x – \alpha }}{2}}}}$ $= \frac{1}{c} cot \frac{{x – \alpha }}{2} + C.$

+ Trường hợp 3: Nếu ${c^2} \ne {a^2} + {b^2}$ thì ta thực hiện phép đổi biến $t = \tan \frac{x}{2}.$

Khi đó: $dx = \frac{{2dt}}{{1 + {t^2}}}$, $\sin x = \frac{{2t}}{{1 + {t^2}}}$ và $\cos x = \frac{{1 – {t^2}}}{{1 + {t^2}}}.$

<!-- chunk:14 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Ví dụ 7: Tìm nguyên hàm: $I = \int {\frac{{2dx}}{{2\sin x – \cos x + 1}}} .$

Đặt $t = \tan \frac{x}{2}$, ta được: $dt = \frac{1}{2} \cdot \frac{1}{{{{\cos }^2}\frac{x}{2}}}dx$ $= \frac{1}{2} \left( {1 + {{\tan }^2}\frac{x}{2}} \right)dx$ $\frac{1}{2}\left( {1 + {t^2}} \right)dx$ $\Rightarrow dx = \frac{{2dt}}{{1 + {t^2}}}.$

Khi đó: $I = \int {\frac{{\frac{{4dt}}{{1 + {t^2}}}}}{{\frac{{4t}}{{1 + {t^2}}} – \frac{{1 – {t^2}}}{{1 + {t^2}}} + 1}}}$ $= \int {\frac{{2dt}}{{{t^2} + 2t}}}$ $= 2\int {\frac{{d(t + 1)}}{{{{(t + 1)}^2} – 1}}}$ $= \ln \left| {\frac{{t – 1}}{{t + 1}}} \right| + C$ $= \ln \left| {\frac{{\tan \frac{x}{2} – 1}}{{\tan \frac{x}{2} + 1}}} \right| + C$ $= \ln \left| {\tan \left( {\frac{x}{2} – \frac{\pi }{4}} \right)} \right| + C.$

<!-- chunk:15 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Dạng 8: Tìm nguyên hàm: $I = \int {\frac{{{a_1}\sin x + {b_1}\cos x + {c_1}}}{{{a_2}\sin x + {b_2}\cos x + {c_2}}}} dx.$

Cách giải: Ta thực hiện theo các bước sau:

+ Bước 1: Biến đổi: ${a_1}\sin x + {b_1}\cos x + {c_1}$ $= A\left( {{a_2}\sin x + {b_2}\cos x + {c_2}} \right) + {\rm{B}}\left( {{a_2}\cos x – {b_2}\sin x} \right) + C.$

+ Bước 2: Khi đó: $I = \int {\frac{{A\left( {{a_2}\sin x + {b_2}\cos x + {c_2}} \right) + B\left( {{a_2}\cos x – {b_2}\sin x} \right) + C}}{{{a_2}\sin x + {b_2}\cos x + {c_2}}}} dx$ $= A\int d x + B\int {\frac{{{a_2}\cos x – {b_2}\sin x}}{{{a_2}\sin x + {b_2}\cos x + {c_2}}}} dx + C\int {\frac{{dx}}{{{a_2}\sin x + {b_2}\cos x + {c_2}}}}$ $= Ax + B\ln \left| {{a_2}\sin x + {b_2}\cos x + {c_2}} \right| + C\int {\frac{{dx}}{{{a_2}\sin x + {b_2}\cos x + {c_2}}}}$, trong đó: $\int {\frac{{dx}}{{{a_2}\sin x + {b_2}\cos x + {c_2}}}}$ được xác định nhờ dạng 4.

<!-- chunk:16 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Ví dụ 8: Tìm họ nguyên hàm của hàm số: $f(x) = \frac{{5\sin x}}{{2\sin x – \cos x + 1}}.$

Giả sử: $5\sin x = a(2\sin x – \cos x + 1) + b(2\cos x + \sin x) + c$ $= (2a + b)\sin x + (2b – a)\cos x + a + c.$

Đồng nhất đẳng thức, ta được: 
$$
\left\{ {\begin{array}{l}
{2a + b = 5}\\
{2b – a = 0}\\
{a + c = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = 2}\\
{b = 1}\\
{c = – 2}
\end{array}} \right.
$$

Khi đó: $f(x) = \frac{{2(2\sin x – \cos x + 1) + (2\cos x + \sin x) – 2}}{{2\sin x – \cos x + 1}}$ $= 2 + \frac{{2\cos x + \sin x}}{{2\sin x – \cos x + 1}} – \frac{2}{{2\sin x – \cos x + 1}}.$

Do đó: $F(x) = \int 2 dx + \int {\frac{{2\cos x + \sin x}}{{2\sin x – \cos x + 1}}} dx – \int {\frac{2}{{2\sin x – \cos x + 1}}} dx$ $= 2\int d x + \int {\frac{{d(2\sin x – \cos x + 1)}}{{2\sin x – \cos x + 1}}} – \int {\frac{{2dx}}{{2\sin x – \cos x + 1}}}$ $= 2x + \ln |2\sin x – \cos x + 1| – \ln \left| {\tan \left( {\frac{x}{2} – \frac{\pi }{4}} \right)} \right| + C.$

Chú ý: Trong lời giải trên ta đã tận dụng kết quả trong ví dụ 7 là: $\int {\frac{{2dx}}{{2\sin x – \cos x + 1}}}$ $= \ln \left| {\tan \left( {\frac{x}{2} – \frac{\pi }{4}} \right)} \right| + C.$

<!-- chunk:17 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Dạng 9: Tìm nguyên hàm: $I = \int {\frac{{{a_1}{{\sin }^2}x + {b_1}\sin x\cos x + {c_1}{{\cos }^2}x}}{{{a_2}\sin x + {b_2}\cos x}}} dx.$
Cách giải: Ta thực hiện theo các bước sau:

+ Bước 1: Biến đổi: ${a_1}{\sin ^2}x + {b_1}\sin x\cos x + {c_1}{\cos ^2}x$ $= \left( {Asin x + B\cos x} \right)\left( {{a_2}\sin x + {b_2}\cos x} \right) + C\left( {{{\sin }^2}x + {{\cos }^2}x} \right).$

+ Bước 2: Khi đó: $I = \int {\frac{{\left( {A\sin x + B\cos x} \right)\left( {{a_2}\sin x + {b_2}\cos x} \right) + C}}{{{a_2}\sin x + {b_2}\cos x}}} dx$ $= \int {\left( {A\sin x + B\cos x} \right)} dx + C\int {\frac{{dx}}{{{a_2}\sin x + {b_2}\cos x}}}$ $= – A\cos x + B\sin x + \frac{C}{{\sqrt {a_2^2 + b_2^2} }}\int {\frac{{dx}}{{\sin (x + \alpha )}}}$ $= – Acos x + Bsin x + \frac{C}{{\sqrt {a_2^2 + b_2^2} }}\ln \left| {\tan \frac{{x + \alpha }}{2}} \right| + C$, trong đó: $\sin \alpha = \frac{{{{\rm{b}}_2}}}{{\sqrt {{\rm{a}}_2^2 + {\rm{b}}_2^2} }}$ và $\cos \alpha = \frac{{{a_2}}}{{\sqrt {a_2^2 + b_2^2} }}.$

<!-- chunk:18 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Ví dụ 9: Tìm họ nguyên hàm của hàm số: $f(x) = \frac{{4{{\sin }^2}x + 1}}{{\sqrt 3 \sin x + \cos x}}.$

Giả sử: $4{\sin ^2}x + 1 = 5{\sin ^2}x + {\cos ^2}x$ $= \left( {asin x + b\cos x} \right)\left( {\sqrt 3 \sin x + \cos x} \right) + c\left( {{{\sin }^2}x + {{\cos }^2}x} \right)$ $= \left( {a\sqrt 3 + c} \right){\sin ^2}x + \left( {a + b\sqrt 3 } \right)\sin x\cos x + \left( {b + c} \right){\cos ^2}x.$

Đồng nhất đẳng thức, ta được: 
$$
\left\{ {\begin{array}{l}
{a\sqrt 3 + c = 5}\\
{a + b\sqrt 3 = 0}\\
{b + c = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = \sqrt 3 }\\
{b = – 1}\\
{c = 2}
\end{array}} \right.
$$

Khi đó: $f(x) = \frac{{\left( {\sqrt 3 \sin x – \cos x} \right)\left( {\sqrt 3 \sin x + \cos x} \right) + 2}}{{\sqrt 3 \sin x + \cos x}}$ $= \sqrt 3 \sin x – \cos x + \frac{2}{{\sqrt 3 \sin x + \cos x}}.$

Do đó: $F(x) = \int {\left( {\sqrt 3 \sin x – \cos x} \right)} dx – \int {\frac{{2dx}}{{\sqrt 3 \sin x + \cos x}}}$ $= – \sqrt 3 \cos x – \sin x – \frac{1}{2}\ln \left| {\tan \left( {\frac{x}{2} + \frac{\pi }{{12}}} \right)} \right| + C.$

Chú ý: Trong lời giải trên ta đã tận dụng kết quả trong ví dụ 4 là: $\int {\frac{{2dx}}{{\sqrt 3 \sin x + \cos x}}} = \frac{1}{2}\ln \left| {\tan \left( {\frac{x}{2} + \frac{\pi }{{12}}} \right)} \right| + C.$

<!-- chunk:19 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Dạng 10: Tìm nguyên hàm: $I = \int {\frac{{dx}}{{a{{\sin }^2}x + b\sin x\cos x + c{{\cos }^2}x}}} .$

Cách giải: Ta thực hiện theo các bước sau:

+ Bước 1: Biến đổi $I$ về dạng: $I = \int {\frac{{dx}}{{\left( {a{{\tan }^2}x + b\tan x + c} \right){{\cos }^2}x}}} .$

+ Bước 2: Thực hiện phép biến đổi: $t = \tan x.$

Suy ra: $dt = \frac{1}{{{{\cos }^2}x}}dx$ và $\frac{{dx}}{{\left( {a{{\tan }^2}x + b\tan x + c} \right){{\cos }^2}x}}$ $= \frac{{dt}}{{a{t^2} + bt + c}}.$

Khi đó: $I = \int {\frac{{dt}}{{a{t^2} + bt + c}}} .$

<!-- chunk:20 level:3 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Ví dụ 10: Tìm nguyên hàm: $I = \int {\frac{{dx}}{{3{{\sin }^2}x – 2\sin x\cos x – {{\cos }^2}x}}} .$

Sử dụng đẳng thức: $\frac{{dx}}{{{{\cos }^2}x}} = d(\tan x).$

Ta có: $I = \int {\frac{{dx}}{{\left( {3{{\tan }^2}x – 2\tan x – 1} \right){{\cos }^2}x}}}$ $= \frac{1}{3}\int {\frac{{d(\tan x)}}{{{{\left( {\tan x – \frac{1}{3}} \right)}^2} – \frac{4}{9}}}}$ $= \frac{1}{3}\int {\frac{{d\left( {\tan x – \frac{1}{3}} \right)}}{{{{\left( {\tan x – \frac{1}{3}} \right)}^2} – \frac{4}{9}}}}$ $= \frac{1}{4}\ln \left| {\frac{{\tan x – \frac{1}{3} – \frac{2}{3}}}{{\tan x – \frac{1}{3} + \frac{2}{3}}}} \right| + C$ $= \frac{1}{4}\ln \left| {\frac{{\tan x – 1}}{{3\tan x + 1}}} \right| + C$ $= \frac{1}{4}\ln \left| {\frac{{\sin x – \cos x}}{{3\sin x + \cos x}}} \right| + C.$

<!-- chunk:21 level:2 source:https://toanmath.com/2018/09/phuong-phap-tim-nguyen-ham-cac-ham-so-luong-giac-phan-1.html -->
## Dạng 11: Tìm nguyên hàm: $I = \int {\frac{{\sin x\cos xdx}}{{{{\left( {{a^2}{{\sin }^2}x + {b^2}{{\cos }^2}x} \right)}^\alpha }}}} .$
Cách giải: Nhận xét rằng: $\sin x\cos xdx$ $= \frac{1}{{2\left( {{a^2} – {b^2}} \right)}}d\left( {{a^2}{{\sin }^2}x + {b^2}{{\cos }^2}x} \right).$

Ta xét 2 trường hợp:

+ Trường hợp 1: Với $α = 1$, ta được: $\int {\frac{{\sin x\cos xdx}}{{{a^2}{{\sin }^2}x + {b^2}{{\cos }^2}x}}}$ $= \frac{1}{{2\left( {{a^2} – {b^2}} \right)}}\int {\frac{{d\left( {{a^2}{{\sin }^2}x + {b^2}{{\cos }^2}x} \right)}}{{{a^2}{{\sin }^2}x + {b^2}{{\cos }^2}x}}}$ $= \frac{1}{{2\left( {{a^2} – {b^2}} \right)}}\ln \left( {{a^2}{{\sin }^2}x + {b^2}{{\cos }^2}x} \right) + C.$

+ Trường hợp 2: Với $α≠1$, ta được: $I = \frac{1}{{2\left( {{a^2} – {b^2}} \right)}}\int {\frac{{d\left( {{a^2}{{\sin }^2}x + {b^2}{{\cos }^2}x} \right)}}{{{{\left( {{a^2}{{\sin }^2}x + {b^2}{{\cos }^2}x} \right)}^\alpha }}}}$ $= \frac{1}{{2\left( {{a^2} – {b^2}} \right)(1 – \alpha )}}{\left( {{a^2}{{\sin }^2}x + {b^2}{{\cos }^2}x} \right)^{ – \alpha + 1}} + C.$

**XEM TIẾP**: Phương pháp tìm nguyên hàm các hàm số lượng giác (Phần 2)