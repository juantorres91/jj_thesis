$Title ArchivoTesis_2
*Conjuntos
Sets
 I   "Conjunto de ingredientes" /Glicerina, Alantoina, Polietilenglicol, PCA, Propilenglicol, Urea, Sorbitol,
                                girasol, almendra, macadamia, avellana, coco, a_oleico, estearico,
                                aceite, petrolato, dimeticona, colesterol, lanonina
                                agua, span80, span60, span40, tween85, tween60, tween80, tween40, tween20,
                                EDTA, sorbatoK, vitC, Fenoxietanol, metilparabeno, propilparabeno, a_sorbico,
                                fragancia, a_citrico, NaOH, a_malico/
 P "Conjunto de preferencias" /humectacion, suavidad, absorcion, grasa, fluidez/
 J "Conjunto de tipo de ingredientes" /humectantes, emolientes, oclusivos, solvente, surfactante, conservantes, fragancia, buffers/
;

*Parámetros
Scalars

 Rsc "Factor de retardo"
 Lsc "Epesor de la SC"    /5.9e-5/
 mu0 "Coeficiente de fricción promedio de la piel" /0.48/
 alpha "Nivel de publicidad de producto" /0.5/
 elast "Elasticidad del producto" /2/
 Presup "Presupuesto del mercado para el producto"
 p2 "Preferecia del producto de la competencia" /0.713397106065432/
 precio2 "Precio del producto de la competencia"
 DemandaT "Demanda total"
 D "Difusividad" /1.30556e-8/


 tinfty "Tiempo de absorción"
*http://www.isn.ucsd.edu/courses/beng221/problems/2012/BENG221_Project%20-%20Ao-Ieong%20Change%20Gu.pdf
;

Parameter
 y(p) "Peso de la preferencia p" /humectacion = 0.3277 , suavidad = 0.1947, absorcion = 0.1841, grasa = 0.1528, fluidez = 0.1407/
 lb(j) "Minima concentración másica del tipo de ingrediente j" /humectantes = 0.0005, emolientes = 0.0005, oclusivos = 0.001, solvente = 0.65, surfactante = 0.01, conservantes = 0.0001, fragancia = 0 , buffers = 0/
 ub(j) "Máxima concentración másica del tipo de ingrediente j" /humectantes = 0.15, emolientes = 0.20, oclusivos = 0.10, solvente = 0.75, surfactante = 0.20, conservantes = 0.10, fragancia = 0.0025 , buffers = 0.02/

 io(i) "1 Si el ingrediente es hidrofobico" /Glicerina = 0, Alantoina = 0, Polietilenglicol = 0, PCA = 0, Propilenglicol = 0, Urea = 0, Sorbitol = 0,
                                            girasol = 1, almendra = 1, macadamia = 1, avellana = 1, coco = 1, a_oleico = 1, estearico = 1,
                                            aceite = 1, petrolato = 1, dimeticona = 1, colesterol = 1, lanonina = 1,
                                            agua = 0, span80 = 1, span60 = 1, span40 = 1, tween85 = 0, tween60 = 0, tween80 = 0, tween40 = 0, tween20 = 0,
                                            EDTA = 0, sorbatoK = 0, vitC = 0, Fenoxietanol = 1, metilparabeno = 1, propilparabeno = 1, a_sorbico = 1
                                            fragancia = 1, a_citrico = 0, NaOH = 0, a_malico = 0/

 nu(i) "Viscosidad cinemática del ingrediente i" /Glicerina = 1119, Alantoina = 1, Polietilenglicol = 7.4, PCA = 1, Propilenglicol = 52, Urea = 1.42, Sorbitol = 85.6,
                                            girasol = 73.45, almendra = 47.2, macadamia = 88.0996, avellana = 65.7, coco = 30, a_oleico = 32.4, estearico = 8.18,
                                            aceite = 34.5, petrolato = 65, dimeticona = 350, colesterol = 6, lanonina = 400,
                                            agua = 0.89, span80 = 1500, span60 = 1000, span40 = 600, tween85 = 300, tween60 = 113.6, tween80 = 370.37, tween40 = 555.56, tween20 = 363.63,
                                            EDTA = 8.5, sorbatoK = 1, vitC = 1, Fenoxietanol = 18, metilparabeno = 1, propilparabeno = 1, a_sorbico = 1
                                            fragancia = 840, a_citrico = 2.24, NaOH = 3, a_malico = 2.24/

 ATE(i) "ATE del ingrediente i" /Glicerina = 2500, Alantoina = 2500, Polietilenglicol = 2500, PCA = 2500, Propilenglicol = 2500, Urea = 2500, Sorbitol = 2500,
                                girasol = 2500, almendra = 2500, macadamia = 2500, avellana = 2500, coco = 2500, a_oleico = 2500, estearico = 2500,
                                aceite = 2500, petrolato = 2500, dimeticona = 2500, colesterol = 2500, lanonina = 2500,
                                agua = 2500, span80 = 2500 , span60 = 2500 , span40 = 2500, tween85 = 2500, tween60 = 2500, tween80 = 2500, tween40 = 2500, tween20 = 2500,
                                EDTA = 1100, sorbatoK = 1100, vitC = 2500, Fenoxietanol = 1100 , metilparabeno = 1100 , propilparabeno = 1100, a_sorbico = 50
                               fragancia = 2500 , a_citrico = 2500 , NaOH = 5, a_malico = 1100/

 rho(i) "Densidad del ingrediente i" /Glicerina = 1.26, Alantoina = 1.45, Polietilenglicol = 1.13, PCA = 1.27, Propilenglicol = 1.04, Urea = 1.32, Sorbitol = 1.49,
                                     girasol = 0.9188, almendra = 0.91, macadamia = 0.9125, avellana = 0.9135, coco = 0.9171, a_oleico = 0.895, estearico = 0.941,
                                     aceite = 0.85, petrolato = 0.852, dimeticona = 0.965, colesterol = 1.05, lanonina = 0.938,
                                     agua = 1, span80 = 0.99 , span60 = 1 , span40 = 1.075, tween85 = 1.028, tween60 = 1.044, tween80 = 1.07, tween40 = 1.05, tween20 = 1.1,
                                     EDTA = 0.860, sorbatoK = 1.36, vitC = 1.69, Fenoxietanol = 1.1 , metilparabeno = 1.46 , propilparabeno = 1.063, a_sorbico = 1.204
                                     fragancia = 0.9 , a_citrico = 1.66 , NaOH = 2.13, a_malico = 1.595/

  HLB(i) "HLB del ingrediente i" /Glicerina = 0, Alantoina = 0, Polietilenglicol = 0, PCA = 0, Propilenglicol = 0, Urea = 0, Sorbitol = 0,
                                girasol = 0, almendra = 0, macadamia = 0, avellana = 0, coco = 0, a_oleico = 0, estearico = 0,
                                aceite = 0, petrolato = 0, dimeticona = 0, colesterol = 0, lanonina = 0
                                agua = 0, span80 = 4.3, span60 = 4.7, span40 = 6.7, tween85 = 11, tween60 = 14.9, tween80 = 15, tween40 = 15.6, tween20 = 16.7,
                                EDTA = 0, sorbatoK = 0, vitC = 0, Fenoxietanol = 0, metilparabeno = 0, propilparabeno = 0, a_sorbico = 0
                                fragancia = 0, a_citrico = 0, NaOH = 0, a_malico = 0/

 cost(i) "Costo del ingrediente i" /Glicerina = 0.0162450396825397, Alantoina = 0.0893716666666667, Polietilenglicol = 0.00926642857142857, PCA = 0.19795, Propilenglicol = 0.0335216346153846, Urea = 0.0151342857142857, Sorbitol = 0.0609629375,
                                   girasol = 0.00854430779277318, almendra = 0.0187240704500978, macadamia = 0.0156362035225048, avellana = 0.014, coco = 0.007698, a_oleico = 0.014, estearico = 0.00674055710738672,
                                   aceite = 0.00803296089385475,  petrolato = 0.00374, dimeticona = 0.016223385, colesterol = 0.242666666666667, lanonina = 0.0154066666666667,
                                   agua = 0.0026, span80 = 0.0178193802373663, span60 = 0.0151666666666667, span40 = 0.0173737373737374, tween85 = 0.0216342412451362, tween60 = 0.0193758182813355, tween80 = 0.0215869158878505, tween40 = 0.0216120382732532, tween20 = 0.0194456116927834,
                                   EDTA = 0.22175, sorbatoK = 0.527075, vitC = 1.02277401960784, Fenoxietanol = 0.112727272727273, metilparabeno = 0.164847272727273, propilparabeno = 0.2572, a_sorbico = 0.1829,
                                   fragancia = 0.0153846153846154, a_citrico = 0.0111386, NaOH = 0.020275, a_malico = 0.030485/
;

table isj(i,j) " si el ingrediente i es del tipo j"
                humectantes      emolientes      oclusivos       solvente        surfactante     conservantes    fragancia      buffers
Glicerina           1                0               0              0                  0               0             0             0
Alantoina           1                0               0              0                  0               0             0             0
Polietilenglicol    1                0               0              0                  0               0             0             0
PCA                 1                0               0              0                  0               0             0             0
Propilenglicol      1                0               0              0                  0               0             0             0
Urea                1                0               0              0                  0               0             0             0
Sorbitol            1                0               0              0                  0               0             0             0
girasol             0                1               0              0                  0               0             0             0
almendra            0                1               0              0                  0               0             0             0
macadamia           0                1               0              0                  0               0             0             0
avellana            0                1               0              0                  0               0             0             0
coco                0                1               0              0                  0               0             0             0
a_oleico            0                1               0              0                  0               0             0             0
estearico           0                1               0              0                  0               0             0             0
aceite              0                0               1              0                  0               0             0             0
petrolato           0                0               1              0                  0               0             0             0
dimeticona          0                0               1              0                  0               0             0             0
colesterol          0                0               1              0                  0               0             0             0
lanonina            0                0               1              0                  0               0             0             0
agua                0                0               0              1                  0               0             0             0
span80              0                0               0              0                  1               0             0             0
span60              0                0               0              0                  1               0             0             0
span40              0                0               0              0                  1               0             0             0
tween85             0                0               0              0                  1               0             0             0
tween60             0                0               0              0                  1               0             0             0
tween80             0                0               0              0                  1               0             0             0
tween40             0                0               0              0                  1               0             0             0
tween20             0                0               0              0                  1               0             0             0
EDTA                0                0               0              0                  0               1             0             0
sorbatoK            0                0               0              0                  0               1             0             0
vitC                0                0               0              0                  0               1             0             0
Fenoxietanol        0                0               0              0                  0               1             0             0
metilparabeno       0                0               0              0                  0               1             0             0
propilparabeno      0                0               0              0                  0               1             0             0
a_sorbico           0                0               0              0                  0               1             0             0
fragancia           0                0               0              0                  0               0             1             0
a_citrico           0                0               0              0                  0               0             0             0
NaOH                0                0               0              0                  0               0             0             0
a_malico            0                0               0              0                  0               0             0             1
;

*Definición de los parámetros
 Rsc = 0.8*0.18 + 0.27 + 0.38;
 tinfty = (0.45*(Lsc**2)*Rsc)/D;
 precio2 = 0.120479432361*0.25;
 Presup = 8648277.12955084*1.75;
 DemandaT = Presup/precio2;

*Variables
Positive Variables

 w(i)    "Fracción másica del ingrediente i"
 wj(j)   "Fracción másica del tipo de ingrediente j"
 woil    "Fracción másica de la fase oleosa"
 wwat    "Fracción másica de la fase acuosa"
* deltamu "Cambio en el coeficiente de ficción (%)"
 mu      "Coeficiente de fricción"
 S       "Suavidad"
 rhooil  "Densidad de la fase oleosa"
 rhowat  "Densidad de la fase acuosa"
 rhotot  "Densidad total de la emulsión"

 nuoil    "Viscosidad cinemática fase oleosa"
 nuwat    "Viscosidad cinemática fase acuosa"
 vis_oil  "Viscosidad dinámica fase oleosa"
 vis_wat  "Viscosidad dinámica fase acuosa"
 kappa    "Relación de viscosidad oleosa y acuosa"
 phioil  "Fracción volumétrica de la faseo oleosa"
 lambda  "Raiz cúbica de la fracción volumétrica de la fase oleosa"
 visco   "Viscosidad dinámica de la emulsión"
 nef     "Raíz cúbica de la viscosidad dinámica"

 ATEmix  "Ate de la mezcla"
 HLBmix  "HLB de la mezcla"

 Preferencia "Preferencia de la loción"
 Ventas "Ventas"
 P1     "Precio"
 d1     "Demanda"
 Costos "Costos"
;

Variables
 VBN(i)  "VBN del ingrediente i"
 VBN_mixo "VBN de la fase oleosa"
 VBN_mixw "VBN de la fase acuosa"
 pref(p) "Puntaje de la preferencia p"
 gamma "Parametro de elasticidad"

;
 pref.lo(p) = 1e-15;
 pref.up(p) = 1.5;
 w.up(i) = 0.75;
 w.lo(i) = 1e-15;
 p1.up = 0.2;

 woil.up = 0.5;
 phioil.up = 0.99;

 kappa.lo = 1e-15;
 lambda.up = 5;
 vis_oil.up = 100;
 vis_wat.up = 100;
* w.l(i) = 1/39;
 p1.l = 0.0826139231901388;
*$ontext
 wj.l('humectantes')= 0.1;
 wj.l('emolientes') = 0.1;
 wj.l('oclusivos') = 0.5;
 wj.l('solvente') = 0.6;
 wj.l('surfactante') = 0.07;
 wj.l('conservantes') = 0.03;
 wj.l('fragancia') = 0.05;
 wj.l('buffers') = 0;

 w.l('Glicerina') =  wj.l('humectantes')/7;
 w.l('Alantoina') = wj.l('humectantes')/7;
 w.l('Polietilenglicol') = wj.l('humectantes')/7;
 w.l('PCA') = wj.l('humectantes')/7;
 w.l('Propilenglicol') = wj.l('humectantes')/7;
 w.l('Urea') = wj.l('humectantes')/7;
 w.l('Sorbitol') = wj.l('humectantes')/7;

 w.l('girasol') =  wj.l('emolientes')/7;
 w.l('almendra') = wj.l('emolientes')/7;
 w.l('macadamia') = wj.l('emolientes')/7;
 w.l('avellana') =  wj.l('emolientes')/7;
 w.l('coco') = wj.l('emolientes')/7;
 w.l('a_oleico') = wj.l('emolientes')/7;
 w.l('estearico') = wj.l('emolientes')/7;

 w.l('aceite') = wj.l('oclusivos')/5;
 w.l('petrolato') = wj.l('oclusivos')/5;
 w.l('dimeticona') = wj.l('oclusivos')/5;
 w.l('colesterol') = wj.l('oclusivos')/5;
 w.l('lanonina') = wj.l('oclusivos')/5;

 w.l('agua') =  wj.l('solvente') ;

 w.l('span80') = wj.l('surfactante')/8;
 w.l('span60') = wj.l('surfactante')/8;
 w.l('span40') = wj.l('surfactante')/8;
 w.l('tween85') = wj.l('surfactante')/8;
 w.l('tween60') = wj.l('surfactante')/8;
 w.l('tween80') = wj.l('surfactante')/8;
 w.l('tween40') = wj.l('surfactante');
 w.l('tween20') = wj.l('surfactante')/8;

 w.l('EDTA') = wj.l('conservantes')/7 ;
 w.l('sorbatoK') = wj.l('conservantes')/7;
 w.l('vitC') = wj.l('conservantes')/7;
 w.l('Fenoxietanol') = wj.l('conservantes')/7;
 w.l('metilparabeno') = wj.l('conservantes')/7;
 w.l('propilparabeno') = wj.l('conservantes')/7;
 w.l('a_sorbico') = wj.l('conservantes')/7;

 w.l('fragancia') = wj.l('fragancia');

 w.l('a_citrico') = wj.l('buffers');
 w.l('NaOH') = wj.l('buffers');
 w.l('a_malico') = wj.l('buffers');

*$offtext


*Restricciones
Equations
 eq_wj(j)
 eq_woil
 eq_wwat
* eq_deltamu
 eq_mu
 eq_s
 eq_rhooil
 eq_rhowat
 eq_rhotot
 eq_VBN(i)
 eq_VBN_mixo
 eq_VBN_mixw
 eq_nuoil
 eq_nuwat
 eq_vis_oil
 eq_vis_wat
 eq_kappa
 eq_phioil
 eq_lambda
 eq_visco
 eq_nef

 eq_pref_Hum
 eq_pref_Suav
 eq_pref_Abs
 eq_pref_Gras
 eq_pref_Flui

 eq_ATEmix
 res_ATEmix

 eq_HLBmix
 res_HLBmix_min
 res_HLBmix_max

 eq_concentracion
 res_concej_min(j)
 res_concej_max(j)

 eq_preferencias
 eq_competencia
 eq_ventas
 eq_costos
 eq_gamma
 res_demanda1
;

*Definición de las restricciones
 eq_wj(j).. wj(j) =e= sum(i, w(i)*isj(i,j));
 eq_woil.. woil =e= sum(i, io(i)*w(i));
 eq_wwat.. wwat =e= 1-woil;
 eq_mu.. mu =e= mu0*(-1.1833*woil + 2.1599);
 eq_s.. s*mu =e= 1;
 eq_rhooil.. rhooil*(sum(i,w(i)*io(i)/rho(i))) =e= woil;
 eq_rhowat.. rhowat*sum(i,w(i)*(1-io(i))/rho(i)) =e= wwat;
 eq_rhotot.. rhotot*sum(i,w(i)/rho(i)) =e= 1;
 eq_VBN(i).. VBN(i) =e= 14.534*log(log(nu(i)+0.8)) + 10.975;
 eq_VBN_mixo.. VBN_mixo*woil =e= sum(i,w(i)*io(i)*VBN(i));
 eq_VBN_mixw.. VBN_mixw*wwat =e= sum(i, w(i)*(1-io(i))*VBN(i));
 eq_nuoil.. nuoil =e= exp(exp((VBN_mixo-10.975)/14.534)) - 0.8;
 eq_nuwat.. nuwat =e= exp(exp((VBN_mixw-10.975)/14.534)) - 0.8;
 eq_vis_oil.. vis_oil =e= nuoil*rhooil;
 eq_vis_wat.. vis_wat =e= nuwat*rhowat;
 eq_kappa.. kappa*vis_wat =e= vis_oil;
 eq_phioil.. phioil*rhooil =e= woil*rhotot;
 eq_lambda.. lambda =e= rpower(phioil, 1/3);
 eq_visco.. visco/100 =e= 1+ 5.5*((4*power(lambda,7)+10)-84/11*power(lambda,2)+4/kappa*(1-power(lambda,7)))/(10*(1-power(lambda,10))-25*power(lambda,3)*(1-power(lambda,4))+10/kappa*(1-power(lambda,3))*(1-power(lambda,7)));
 eq_nef.. nef =e= rpower(visco,1/3);

 eq_pref_Hum.. pref('humectacion') =e= -21788.5*(power(wj('humectantes'),5)+power(wj('emolientes'),5)) + 13978*(power(wj('humectantes'),4)+power(wj('emolientes'),4)) - 3203.4*(power(wj('humectantes'),3)+power(wj('emolientes'),3)) + 290.32*(power(wj('humectantes'),2)+power(wj('emolientes'),2)) - 4.4861*(wj('humectantes')+wj('emolientes')) + 0.039734;
 eq_pref_Suav.. pref('suavidad') =e= 256.57*power(S,3) - 865.47*power(S,2) + 975.21*S - 366.13;
 eq_pref_Abs.. pref('absorcion') =e= 4e-9*power(tinfty,3) - 6e-6*power(tinfty,2) + 6e-4*tinfty + 0.9848;
 eq_pref_Gras.. pref('grasa') =e= 35.85*rpower(woil,3/2) - 69.618*rpower(woil,2/2) + 36.418*rpower(woil,1/2) - 4.6881;
 eq_pref_Flui.. pref('fluidez') =e= 0.002*rpower(nef,3)-0.069*rpower(nef,2)+ 0.6835*rpower(nef,1) -1.0402;

 eq_ATEmix.. ATEmix*sum(i,w(i)/ATE(i)) =e= 1;
 res_ATEmix.. ATEmix =g= 1200;

 eq_HLBmix..  HLBmix*wj('surfactante') =e= sum(i, w(i)*HLB(i));
 res_HLBmix_min..  HLBmix =g= 8;
 res_HLBmix_max..  HLBmix =l= 18;

 eq_concentracion.. sum(i,w(i)) =e= 1;
 res_concej_min(j).. wj(j) =g=  lb(j);
 res_concej_max(j).. wj(j) =l= ub(j);

 eq_preferencias.. Preferencia =e= sum(p,pref(p)*y(p));
 eq_ventas.. Ventas =e= P1*d1;
 eq_costos.. Costos =e= sum(i,cost(i)*w(i)*d1);

 eq_competencia .. p1*d1 =e= rpower((alpha*Preferencia/p2),elast)*precio2*rpower(((Presup-p1*d1)/precio2),1-elast)*rpower(d1,elast);
 eq_gamma.. gamma =e= rpower((alpha*preferencia/p2),(elast/(elast-1)));
 res_demanda1.. d1 =e= DemandaT/(1+ gamma);


*Función Objetivo
Variable
 zobj "Variable objetivo"
;

Equation
 fobj  "Función objetivo"
;
* fobj..zobj =e= d1;
 fobj..zobj =e= Ventas - Costos;
* fobj..zobj =e= Preferencia;

model ArchivoTesis_2 /all/;
options nlp = ipopt;
execute_loadpoint 'ArchivoTesis_Final';
solve ArchivoTesis_2 using nlp maximizing zobj;
execute_unload "ArchivoTesis_2.gdx"

