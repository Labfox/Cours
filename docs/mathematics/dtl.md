# DTL 3
## Exercice 1
### 1)
L'aire du carré correspond à $x^2$

### 2)

L'aire d'un rectangle peut être calculée avec la formule suivante : $longueur * largeur$.
Dans le cas de ce triangle, la largeur est égale à $x - 3$ et la longueur est égale à $x + 7$, donnant
$(x-3) * (x+7)$.

Maintenant, il suffit de développer et de réduire $(x-3) * (x+7)$:

- $x^2 + 7x - 3x - 3*7$
- $x^2 + 4x - 21$

**L'aire du rectangle est donc égale à $x^2 + 4x - 21$**

### 3)

Pour la ligne 5, le contenu est $4$, pour la ligne 6, le contenu est $-21$, et pour la ligne 7, 
le contenu est x (en tant que variable).

### 4)

Dans ce cas, le programme calculera $x^2 + 4x - 21$ avec $x=8$:

- $8^2 + 4*8 - 21$
- $64 + 32 - 21$
- $75$

**Le résultat sera donc $75$**

### 5)

Pour que l'aire du rectangle soit égale à l'aire du carré, il faut trouver une situation ou 
$x^2 = x^2 + 4x - 21$.

Nous résolvons donc l'équation :

- $x^2 - x^2  = x^2 + 4x - 21 - x^2$ **->** $0  = 4x - 21$
- $0 + 21  = 4x - 21 + 21$ **->** $21 = 4x$
- $21 / 4 = 4x / 4$ **->** $5.25 = x$

Vérification:

- $5.25^2 = 5.25^2 + 4*5.25 - 21$ **->** $27.5625 = 27.5625 + 21 - 21$
- $27.5625 = 27.5625$

**La valeur de $x$ pour que l'aire du carré et l'aire du rectangle soient égaux est donc $5.25$**

## Exercice 2
### 1)
#### a)

On considère $p$ un nombre tel que $0 < p < \infty$ représentant la profondeur de l'escalator.
Selon l'énoncé on à 5 escalators ($5p$), 6 passerelles horizontales de $12,5$m ($6*12,5$), le tout sur
une surface de $135$m. Celà donne donc $135 = 5p + 6 * 12,5$.

On résout donc $135 = 5p + 6 * 12,5$:

- $135 - 75 = 5p + 75 - 75$ **->** $60 = 5p$
- $60 / 5 = 5p / 5$ **->** $12 = p$.

**La profondeur de chaque escalator est donc bien $12$**

#### b)

On considère maintenant $h$ un nombre tel que $0 < h < \infty$ représentant la hauteur de l'escalator.
Selon l'énoncé, il y à 5 escalators ($5h$), répartis sur $32$m de hauteur (on ignore les passerelles
horizontales ayant une hauteur de 0. Celà donne donc $32 = 5h$. 

En résolvant, celà donne $h=6.4$ (division des deux parties par 5).

**La hauteur de chaque escalator est donc $6.4$m**

### 2)
#### a)

$RST$ étant un triangle-rectangle en $\widehat R$, on peut utiliser le théorème de Pythagore :
$TS^2 = SR^2 + TR^2$. Nous avons donc $TS^2 = 12^2 + 6,4^2$, $TS^2 = 144 + 40.96$, 
donc $TS = \sqrt {184.96}$. **La longueur ST est donc 13.6.**

#### b)

Nous pouvons effectuer le cosinus de $\widehat {RST}$: $SR / TS$, étant égal à approximativement
$0.8823529411$. Nous effectuons donc $\arccos (0.8823529411)$ pour obtenir l'angle, donnant 
approximativement $28.0724°$. **L'angle $\widehat {RST}$ arrondi au degré est donc bien $28°$.**

### 3)

En ligne 6, la valeur est $5$, en ligne 7, la valeur est de $12,5$, en ligne 9, la valeur est de $12$,
et en ligne 10, la valeur est de $-28$