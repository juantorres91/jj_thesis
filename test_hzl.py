juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ pysp
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
3 Param Declarations
    H : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :     1
    di : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :   0.9
    dt : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :     1

5 Var Declarations
    N : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals
    Po : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   0.1 :  None : False : False : PositiveReals
    m_time : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals
    mu : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 : 0.001 :  None : False : False : PositiveReals
    rho : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   997 :  None : False : False : PositiveReals

1 Constraint Declarations
    mixing_eq : Size=1, Index=None, Active=True
        Key  : Lower : Body                                                           : Upper : Active
        None :   0.0 : m_time - 5.2 * dt**1.5 * H**0.5 / ( di**2.0 * Po**0.3333 * N ) :   0.0 :   True

9 Declarations: di dt H rho mu Po N m_time mixing_eq
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$         None :   0.0 : m_time - 5.2 * dt**1.5 * H**0.5 / ( di**2.0 * Po**0.3333 * N ) :   0.0 :   True

9 Declarations: di dt H rho mu Po N m_time mixing_eq
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ 
bash: syntax error near unexpected token `('
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ (pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ 9: command not found
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ bash: syntax error near unexpected token `juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
ERROR: Rule failed when generating expression for constraint mixing_eq:
    AttributeError: 'module' object has no attribute 'pow'
ERROR: Constructing component 'mixing_eq' from data=None failed:
    AttributeError: 'module' object has no attribute 'pow'
Traceback (most recent call last):
  File "test_pre.py", line 41, in <module>
    m = premixing_model()
  File "test_pre.py", line 33, in premixing_model
    m.mixing_eq = pe.Constraint(rule = turbulent_mix_rule)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 542, in __setattr__
    self.add_component(name, val)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 970, in add_component
    val.construct(data)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/constraint.py", line 742, in construct
    tmp = _init_rule(_self_parent)
  File "test_pre.py", line 5, in turbulent_mix_rule
    return m.m_time == 5.20 * (m.dt**1.5)*(m.H**0.5) / (m.di**2 * pe.pow(m.Po, 1/3)  * m.N)  
AttributeError: 'module' object has no attribute 'pow'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
3 Param Declarations
    H : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :     1
    di : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :   0.9
    dt : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :     1

5 Var Declarations
    N : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals
    Po : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   0.1 :  None : False : False : PositiveReals
    m_time : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals
    mu : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 : 0.001 :  None : False : False : PositiveReals
    rho : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   997 :  None : False : False : PositiveReals

1 Constraint Declarations
    mixing_eq : Size=1, Index=None, Active=True
        Key  : Lower : Body                                                              : Upper : Active
        None :   0.0 : m_time - 5.2 * dt**1.5 * H**0.5 / ( di**2.0 * Po**0.3333334 * N ) :   0.0 :   True

9 Declarations: di dt H rho mu Po N m_time mixing_eq
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
ERROR: Rule failed when generating expression for constraint mixing_eq:
    AttributeError: 'module' object has no attribute 'pow'
ERROR: Constructing component 'mixing_eq' from data=None failed:
    AttributeError: 'module' object has no attribute 'pow'
Traceback (most recent call last):
  File "test_pre.py", line 41, in <module>
    m = premixing_model(model='transition')
  File "test_pre.py", line 35, in premixing_model
    m.mixing_eq = pe.Constraint(rule = transition_mix_rule)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 542, in __setattr__
    self.add_component(name, val)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 970, in add_component
    val.construct(data)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/constraint.py", line 742, in construct
    tmp = _init_rule(_self_parent)
  File "test_pre.py", line 8, in transition_mix_rule
    return m.m_time == (183)**2 * (m.dt**1.5)*(m.H**0.5)*(m.mu)/(m.rho * pe.pow(m.Po, 0.666667) * pe.pow(m.N,2) * pe.pow(m.di, 4) )  
AttributeError: 'module' object has no attribute 'pow'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
3 Param Declarations
    H : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :     1
    di : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :   0.9
    dt : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :     1

5 Var Declarations
    N : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals
    Po : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   0.1 :  None : False : False : PositiveReals
    m_time : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals
    mu : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 : 0.001 :  None : False : False : PositiveReals
    rho : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   997 :  None : False : False : PositiveReals

1 Constraint Declarations
    mixing_eq : Size=1, Index=None, Active=True
        Key  : Lower : Body                                                                                 : Upper : Active
        None :   0.0 : m_time - 33489.0 * dt**1.5 * H**0.5 * mu / ( rho * Po**0.666667 * N**2.0 * di**4.0 ) :   0.0 :   True

9 Declarations: di dt H rho mu Po N m_time mixing_eq
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
ERROR: Rule failed when generating expression for constraint
    re_turbulent.mixing_eq: AttributeError: 'SimpleDisjunct' object has no
    attribute 'm_time'
ERROR: Constructing component 're_turbulent.mixing_eq' from data=None failed:
    AttributeError: 'SimpleDisjunct' object has no attribute 'm_time'
Traceback (most recent call last):
  File "test_pre.py", line 52, in <module>
    m = premixing_model(model='hybrid')
  File "test_pre.py", line 44, in premixing_model
    m.re_turbulent.mixing_eq = pe.Constraint(rule = turbulent_mix_rule)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 542, in __setattr__
    self.add_component(name, val)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 970, in add_component
    val.construct(data)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/constraint.py", line 742, in construct
    tmp = _init_rule(_self_parent)
  File "test_pre.py", line 5, in turbulent_mix_rule
    return m.m_time == 5.20 * (m.dt**1.5)*(m.H**0.5) / (m.di**2 * pow(m.Po, 0.3333334)  * m.N)  
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 523, in __getattr__
    % (self.__class__.__name__, val))
AttributeError: 'SimpleDisjunct' object has no attribute 'm_time'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
3 Param Declarations
    H : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :     1
    di : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :   0.9
    dt : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :     1

5 Var Declarations
    N : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals
    Po : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   0.1 :  None : False : False : PositiveReals
    m_time : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals
    mu : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 : 0.001 :  None : False : False : PositiveReals
    rho : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   997 :  None : False : False : PositiveReals

1 Constraint Declarations
    mixing_eq : Size=1, Index=None, Active=True
        Key  : Lower : Body                                                                                 : Upper : Active
        None :   0.0 : m_time - 33489.0 * dt**1.5 * H**0.5 * mu / ( rho * Po**0.666667 * N**2.0 * di**4.0 ) :   0.0 :   True

9 Declarations: di dt H rho mu Po N m_time mixing_eq
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
3 Param Declarations
    H : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :     1
    di : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :   0.9
    dt : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :     1

5 Var Declarations
    N : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals
    Po : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   0.1 :  None : False : False : PositiveReals
    m_time : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals
    mu : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 : 0.001 :  None : False : False : PositiveReals
    rho : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   997 :  None : False : False : PositiveReals

1 Constraint Declarations
    mixing_eq : Size=1, Index=None, Active=True
        Key  : Lower : Body                                                              : Upper : Active
        None :   0.0 : m_time - 5.2 * dt**1.5 * H**0.5 / ( di**2.0 * Po**0.3333334 * N ) :   0.0 :   True

9 Declarations: di dt H rho mu Po N m_time mixing_eq
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
ERROR: Rule failed when generating expression for constraint
    re_turbulent.mixing_eq: AttributeError: 'SimpleDisjunct' object has no
    attribute 'm_time'
ERROR: Constructing component 're_turbulent.mixing_eq' from data=None failed:
    AttributeError: 'SimpleDisjunct' object has no attribute 'm_time'
Traceback (most recent call last):
  File "test_pre.py", line 52, in <module>
    m = premixing_model(model='hybrid')
  File "test_pre.py", line 44, in premixing_model
    m.re_turbulent.mixing_eq = pe.Constraint(rule = turbulent_mix_rule)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 542, in __setattr__
    self.add_component(name, val)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 970, in add_component
    val.construct(data)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/constraint.py", line 742, in construct
    tmp = _init_rule(_self_parent)
  File "test_pre.py", line 5, in turbulent_mix_rule
    return m.m_time == 5.20 * (m.dt**1.5)*(m.H**0.5) / (m.di**2 * pow(m.Po, 0.3333334)  * m.N)  
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 523, in __getattr__
    % (self.__class__.__name__, val))
AttributeError: 'SimpleDisjunct' object has no attribute 'm_time'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
ERROR: Rule failed when generating expression for constraint
    re_transition.mixing_eq: AttributeError: 'SimpleDisjunct' object has no
    attribute 'm_time'
ERROR: Constructing component 're_transition.mixing_eq' from data=None failed:
    AttributeError: 'SimpleDisjunct' object has no attribute 'm_time'
Traceback (most recent call last):
  File "test_pre.py", line 52, in <module>
    m = premixing_model(model='hybrid')
  File "test_pre.py", line 45, in premixing_model
    m.re_transition.mixing_eq = pe.Constraint(rule = transition_mix_rule)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 542, in __setattr__
    self.add_component(name, val)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 970, in add_component
    val.construct(data)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/constraint.py", line 742, in construct
    tmp = _init_rule(_self_parent)
  File "test_pre.py", line 8, in transition_mix_rule
    return m.m_time == (183)**2 * (m.dt**1.5)*(m.H**0.5)*(m.mu)/(m.rho * pow(m.Po, 0.666667) * pow(m.N,2) * pow(m.di, 4) )  
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 523, in __getattr__
    % (self.__class__.__name__, val))
AttributeError: 'SimpleDisjunct' object has no attribute 'm_time'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
ERROR: Rule failed when generating expression for constraint
    re_transition.mixing_eq: AttributeError: 'SimpleDisjunct' object has no
    attribute 'm_time'
ERROR: Constructing component 're_transition.mixing_eq' from data=None failed:
    AttributeError: 'SimpleDisjunct' object has no attribute 'm_time'
Traceback (most recent call last):
  File "test_pre.py", line 52, in <module>
    m = premixing_model(model='hybrid')
  File "test_pre.py", line 45, in premixing_model
    m.re_transition.mixing_eq = pe.Constraint(rule = transition_mix_rule)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 542, in __setattr__
    self.add_component(name, val)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 970, in add_component
    val.construct(data)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/constraint.py", line 742, in construct
    tmp = _init_rule(_self_parent)
  File "test_pre.py", line 8, in transition_mix_rule
    return m.m_time == (183)**2 * (m.dt**1.5)*(m.H**0.5)*(m.mu)/(m.rho * pow(m.Po, 0.666667) * pow(m.N,2) * pow(m.di, 4) )  
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 523, in __getattr__
    % (self.__class__.__name__, val))
AttributeError: 'SimpleDisjunct' object has no attribute 'm_time'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
ERROR: Rule failed when generating expression for constraint
    re_transition.mixing_eq: AttributeError: 'SimpleDisjunct' object has no
    attribute 'm_time'
ERROR: Constructing component 're_transition.mixing_eq' from data=None failed:
    AttributeError: 'SimpleDisjunct' object has no attribute 'm_time'
Traceback (most recent call last):
  File "test_pre.py", line 52, in <module>
    m = premixing_model(model='hybrid')
  File "test_pre.py", line 45, in premixing_model
    m.re_transition.mixing_eq = pe.Constraint(rule = transition_mix_rule)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 542, in __setattr__
    self.add_component(name, val)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 970, in add_component
    val.construct(data)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/constraint.py", line 742, in construct
    tmp = _init_rule(_self_parent)
  File "test_pre.py", line 8, in transition_mix_rule
    return m.m_time == (183)**2 * (m.dt**1.5)*(m.H**0.5)*(m.mu)/(m.rho * pow(m.Po, 0.666667) * pow(m.N,2) * pow(m.di, 4) )  
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 523, in __getattr__
    % (self.__class__.__name__, val))
AttributeError: 'SimpleDisjunct' object has no attribute 'm_time'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
ERROR: Rule failed when generating expression for constraint
    re_turbulent.mixing_eq: AttributeError: 'SimpleDisjunct' object has no
    attribute 'm_time'
ERROR: Constructing component 're_turbulent.mixing_eq' from data=None failed:
    AttributeError: 'SimpleDisjunct' object has no attribute 'm_time'
Traceback (most recent call last):
  File "test_pre.py", line 52, in <module>
    m = premixing_model(model='hybrid')
  File "test_pre.py", line 44, in premixing_model
    m.re_turbulent.mixing_eq = pe.Constraint(rule = turbulent_mix_rule)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 542, in __setattr__
    self.add_component(name, val)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 970, in add_component
    val.construct(data)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/constraint.py", line 742, in construct
    tmp = _init_rule(_self_parent)
  File "test_pre.py", line 5, in turbulent_mix_rule
    return m.m_time == 5.20 * (m.dt**1.5)*(m.H**0.5) / (m.di**2 * pow(m.Po, 0.3333334)  * m.N)  
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 523, in __getattr__
    % (self.__class__.__name__, val))
AttributeError: 'SimpleDisjunct' object has no attribute 'm_time'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
3 Param Declarations
    H : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :     1
    di : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :   0.9
    dt : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
        Key  : Value
        None :     1

5 Var Declarations
    N : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals
    Po : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   0.1 :  None : False : False : PositiveReals
    m_time : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :  None :  None :  None : False :  True :  Reals
    mu : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 : 0.001 :  None : False : False : PositiveReals
    rho : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   997 :  None : False : False : PositiveReals

2 Disjunct Declarations
    re_transition : Size=1, Index=None, Active=True
        1 Var Declarations
            indicator_var : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :  None :     1 : False :  True : Binary

        1 Constraint Declarations
            mixing_eq : Size=1, Index=None, Active=True
                Key  : Lower : Body                                                                                 : Upper : Active
                None :   0.0 : m_time - 33489.0 * dt**1.5 * H**0.5 * mu / ( rho * Po**0.666667 * N**2.0 * di**4.0 ) :   0.0 :   True

        2 Declarations: indicator_var mixing_eq
    re_turbulent : Size=1, Index=None, Active=True
        1 Var Declarations
            indicator_var : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :  None :     1 : False :  True : Binary

        1 Constraint Declarations
            mixing_eq : Size=1, Index=None, Active=True
                Key  : Lower : Body                                                              : Upper : Active
                None :   0.0 : m_time - 5.2 * dt**1.5 * H**0.5 / ( di**2.0 * Po**0.3333334 * N ) :   0.0 :   True

        2 Declarations: indicator_var mixing_eq

10 Declarations: di dt H rho mu Po N m_time re_turbulent re_transition
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python test_pre.py
python: can't open file 'test_pre.py': [Errno 2] No such file or directory
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python testing.py
1 Block Declarations
    pre_mix : Size=1, Index=None, Active=True
        3 Param Declarations
            H : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
                Key  : Value
                None :     1
            di : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
                Key  : Value
                None :   0.9
            dt : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
                Key  : Value
                None :     1

        5 Var Declarations
            N : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :  None :  None : False :  True : PositiveReals
            Po : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :   0.1 :  None : False : False : PositiveReals
            m_time : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :  None :  None :  None : False :  True :  Reals
            mu : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 : 0.001 :  None : False : False : PositiveReals
            rho : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :   997 :  None : False : False : PositiveReals

        2 Disjunct Declarations
            re_transition : Size=1, Index=None, Active=True
                1 Var Declarations
                    indicator_var : Size=1, Index=None
                        Key  : Lower : Value : Upper : Fixed : Stale : Domain
                        None :     0 :  None :     1 : False :  True : Binary

                1 Constraint Declarations
                    mixing_eq : Size=1, Index=None, Active=True
                        Key  : Lower : Body                                                                                                                                                 : Upper : Active
                        None :   0.0 : pre_mix.m_time - 33489.0 * pre_mix.dt**1.5 * pre_mix.H**0.5 * pre_mix.mu / ( pre_mix.rho * pre_mix.Po**0.666667 * pre_mix.N**2.0 * pre_mix.di**4.0 ) :   0.0 :   True

                2 Declarations: indicator_var mixing_eq
            re_turbulent : Size=1, Index=None, Active=True
                1 Var Declarations
                    indicator_var : Size=1, Index=None
                        Key  : Lower : Value : Upper : Fixed : Stale : Domain
                        None :     0 :  None :     1 : False :  True : Binary

                1 Constraint Declarations
                    mixing_eq : Size=1, Index=None, Active=True
                        Key  : Lower : Body                                                                                                              : Upper : Active
                        None :   0.0 : pre_mix.m_time - 5.2 * pre_mix.dt**1.5 * pre_mix.H**0.5 / ( pre_mix.di**2.0 * pre_mix.Po**0.3333334 * pre_mix.N ) :   0.0 :   True

                2 Declarations: indicator_var mixing_eq

        10 Declarations: di dt H rho mu Po N m_time re_turbulent re_transition

1 Declarations: pre_mix
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python testing.py
Traceback (most recent call last):
  File "testing.py", line 8, in <module>
    m.Reynolds = pe.Var(within = PositiveReals)
NameError: name 'PositiveReals' is not defined
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python testing.py
Traceback (most recent call last):
  File "testing.py", line 11, in <module>
    m.pre_mix.re_turbulent.re_cons( expr = m.Reynolds >= 1e4)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 523, in __getattr__
    % (self.__class__.__name__, val))
AttributeError: 'SimpleDisjunct' object has no attribute 're_cons'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python testing.py
1 Var Declarations
    Reynolds : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals

1 Block Declarations
    pre_mix : Size=1, Index=None, Active=True
        3 Param Declarations
            H : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
                Key  : Value
                None :     1
            di : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
                Key  : Value
                None :   0.9
            dt : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
                Key  : Value
                None :     1

        5 Var Declarations
            N : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :  None :  None : False :  True : PositiveReals
            Po : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :   0.1 :  None : False : False : PositiveReals
            m_time : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :  None :  None :  None : False :  True :  Reals
            mu : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 : 0.001 :  None : False : False : PositiveReals
            rho : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :   997 :  None : False : False : PositiveReals

        2 Disjunct Declarations
            re_transition : Size=1, Index=None, Active=True
                1 Var Declarations
                    indicator_var : Size=1, Index=None
                        Key  : Lower : Value : Upper : Fixed : Stale : Domain
                        None :     0 :  None :     1 : False :  True : Binary

                2 Constraint Declarations
                    mixing_eq : Size=1, Index=None, Active=True
                        Key  : Lower : Body                                                                                                                                                 : Upper : Active
                        None :   0.0 : pre_mix.m_time - 33489.0 * pre_mix.dt**1.5 * pre_mix.H**0.5 * pre_mix.mu / ( pre_mix.rho * pre_mix.Po**0.666667 * pre_mix.N**2.0 * pre_mix.di**4.0 ) :   0.0 :   True
                    re_cons : Size=1, Index=None, Active=True
                        Key  : Lower : Body     : Upper  : Active
                        None :  -Inf : Reynolds : 9000.0 :   True

                3 Declarations: indicator_var mixing_eq re_cons
            re_turbulent : Size=1, Index=None, Active=True
                1 Var Declarations
                    indicator_var : Size=1, Index=None
                        Key  : Lower : Value : Upper : Fixed : Stale : Domain
                        None :     0 :  None :     1 : False :  True : Binary

                2 Constraint Declarations
                    mixing_eq : Size=1, Index=None, Active=True
                        Key  : Lower : Body                                                                                                              : Upper : Active
                        None :   0.0 : pre_mix.m_time - 5.2 * pre_mix.dt**1.5 * pre_mix.H**0.5 / ( pre_mix.di**2.0 * pre_mix.Po**0.3333334 * pre_mix.N ) :   0.0 :   True
                    re_cons : Size=1, Index=None, Active=True
                        Key  : Lower   : Body     : Upper : Active
                        None : 10000.0 : Reynolds :  +Inf :   True

                3 Declarations: indicator_var mixing_eq re_cons

        10 Declarations: di dt H rho mu Po N m_time re_turbulent re_transition

2 Declarations: pre_mix Reynolds
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python testing.py
ERROR: Rule failed when generating expression for constraint regim:
    ValueError: Non-disjunct (type="<class
    'pyomo.core.base.constraint.SimpleConstraint'>") found in disjunctive set
    for disjunction regim
ERROR: Constructing component 'regim' from data=None failed: ValueError: Non-
    disjunct (type="<class 'pyomo.core.base.constraint.SimpleConstraint'>")
    found in disjunctive set for disjunction regim
Traceback (most recent call last):
  File "testing.py", line 16, in <module>
    m.regim = gdp.Disjunction(expr = [m.pre_mix.re_turbulent.re_cons, m.pre_mix.re_transition.re_cons])  
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 542, in __setattr__
    self.add_component(name, val)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 970, in add_component
    val.construct(data)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/constraint.py", line 742, in construct
    tmp = _init_rule(_self_parent)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/gdp/disjunct.py", line 352, in __call__
    raise ValueError(msg)
ValueError: Non-disjunct (type="<class 'pyomo.core.base.constraint.SimpleConstraint'>") found in disjunctive set for disjunction regim
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python testing.py
ERROR: Rule failed when generating expression for constraint regim:
    ValueError: Non-disjunct (type="<class
    'pyomo.core.base.constraint.SimpleConstraint'>") found in disjunctive set
    for disjunction regim
ERROR: Constructing component 'regim' from data=None failed: ValueError: Non-
    disjunct (type="<class 'pyomo.core.base.constraint.SimpleConstraint'>")
    found in disjunctive set for disjunction regim
Traceback (most recent call last):
  File "testing.py", line 17, in <module>
    m.regim = gdp.Disjunction(expr = [m.pre_mix.re_turbulent.re_cons, m.pre_mix.re_transition.re_cons])  
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 542, in __setattr__
    self.add_component(name, val)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 970, in add_component
    val.construct(data)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/constraint.py", line 742, in construct
    tmp = _init_rule(_self_parent)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/gdp/disjunct.py", line 352, in __call__
    raise ValueError(msg)
ValueError: Non-disjunct (type="<class 'pyomo.core.base.constraint.SimpleConstraint'>") found in disjunctive set for disjunction regim
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$     m.regim = gdp.Disjunction(expr = [m.pre_mix.re_turbulent.re_cons, m.pre_mix.re_transition.re_cons])  
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 542, in __setattr__
    self.add_component(name, val)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/block.py", line 970, in add_component
    val.construct(data)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/core/base/constraint.py", line 742, in construct
    tmp = _init_rule(_self_parent)
  File "/home/juan/anaconda2/envs/pysp_test/lib/python2.7/site-packages/pyomo/gdp/disjunct.py", line 352, in __call__
    raise ValueError(msg)
ValueError: Non-disjunct (type="<class 'pyomo.core.base.constraint.SimpleConstraint'>") found in disjunctive set for disjunction regim
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ 
bash: syntax error near unexpected token `('
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ No command 'File' found, did you mean:
 Command 'kile' from package 'kile' (universe)
 Command 'zile' from package 'zile' (universe)
 Command 'file' from package 'file' (main)
 Command 'vile' from package 'vile' (universe)
File: command not found
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ bash: syntax error near unexpected token `name,'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ No command 'File' found, did you mean:
 Command 'kile' from package 'kile' (universe)
 Command 'zile' from package 'zile' (universe)
 Command 'vile' from package 'vile' (universe)
 Command 'file' from package 'file' (main)
File: command not found
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ bash: syntax error near unexpected token `data'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ No command 'File' found, did you mean:
 Command 'kile' from package 'kile' (universe)
 Command 'vile' from package 'vile' (universe)
 Command 'zile' from package 'zile' (universe)
 Command 'file' from package 'file' (main)
File: command not found
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ bash: syntax error near unexpected token `('
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ No command 'File' found, did you mean:
 Command 'kile' from package 'kile' (universe)
 Command 'vile' from package 'vile' (universe)
 Command 'file' from package 'file' (main)
 Command 'zile' from package 'zile' (universe)
File: command not found
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ bash: syntax error near unexpected token `('
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ bash: syntax error near unexpected token `('
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ bash: syntax error near unexpected token `juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python testing.py
1 Var Declarations
    Reynolds : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals

1 Block Declarations
    pre_mix : Size=1, Index=None, Active=True
        3 Param Declarations
            H : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
                Key  : Value
                None :     1
            di : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
                Key  : Value
                None :   0.9
            dt : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
                Key  : Value
                None :     1

        5 Var Declarations
            N : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :  None :  None : False :  True : PositiveReals
            Po : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :   0.1 :  None : False : False : PositiveReals
            m_time : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :  None :  None :  None : False :  True :  Reals
            mu : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 : 0.001 :  None : False : False : PositiveReals
            rho : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :   997 :  None : False : False : PositiveReals

        2 Disjunct Declarations
            re_transition : Size=1, Index=None, Active=True
                1 Var Declarations
                    indicator_var : Size=1, Index=None
                        Key  : Lower : Value : Upper : Fixed : Stale : Domain
                        None :     0 :  None :     1 : False :  True : Binary

                2 Constraint Declarations
                    mixing_eq : Size=1, Index=None, Active=True
                        Key  : Lower : Body                                                                                                                                                 : Upper : Active
                        None :   0.0 : pre_mix.m_time - 33489.0 * pre_mix.dt**1.5 * pre_mix.H**0.5 * pre_mix.mu / ( pre_mix.rho * pre_mix.Po**0.666667 * pre_mix.N**2.0 * pre_mix.di**4.0 ) :   0.0 :   True
                    re_cons : Size=1, Index=None, Active=True
                        Key  : Lower : Body     : Upper  : Active
                        None :  -Inf : Reynolds : 9000.0 :   True

                3 Declarations: indicator_var mixing_eq re_cons
            re_turbulent : Size=1, Index=None, Active=True
                1 Var Declarations
                    indicator_var : Size=1, Index=None
                        Key  : Lower : Value : Upper : Fixed : Stale : Domain
                        None :     0 :  None :     1 : False :  True : Binary

                2 Constraint Declarations
                    mixing_eq : Size=1, Index=None, Active=True
                        Key  : Lower : Body                                                                                                              : Upper : Active
                        None :   0.0 : pre_mix.m_time - 5.2 * pre_mix.dt**1.5 * pre_mix.H**0.5 / ( pre_mix.di**2.0 * pre_mix.Po**0.3333334 * pre_mix.N ) :   0.0 :   True
                    re_cons : Size=1, Index=None, Active=True
                        Key  : Lower   : Body     : Upper : Active
                        None : 10000.0 : Reynolds :  +Inf :   True

                3 Declarations: indicator_var mixing_eq re_cons

        10 Declarations: di dt H rho mu Po N m_time re_turbulent re_transition

1 Disjunction Declarations
    regim : Size=1, Index=None, Active=True
        Key  : Lower : Body                                                                     : Upper : Active
        None :   1.0 : pre_mix.re_turbulent.indicator_var + pre_mix.re_transition.indicator_var :   1.0 :   True

3 Declarations: pre_mix Reynolds regim
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python testing.py
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ python testing.py
1 Var Declarations
    Reynolds : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True : PositiveReals

2 Block Declarations
    _gdp_relax_bigm : Size=1, Index=None, Active=True
        1 Constraint Declarations
            regim : Size=1, Index=None, Active=True
                Key  : Lower : Body                                                                                                     : Upper : Active
                None :   1.0 : pre_mix._gdp_relax_bigm.re_turbulent.indicator_var + pre_mix._gdp_relax_bigm.re_transition.indicator_var :   1.0 :   True

        1 Declarations: regim
    pre_mix : Size=1, Index=None, Active=True
        3 Param Declarations
            H : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
                Key  : Value
                None :     1
            di : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
                Key  : Value
                None :   0.9
            dt : Size=1, Index=None, Domain=Any, Default=None, Mutable=True
                Key  : Value
                None :     1

        5 Var Declarations
            N : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :  None :  None : False :  True : PositiveReals
            Po : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :   0.1 :  None : False : False : PositiveReals
            m_time : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :  None :  None :  None : False :  True :  Reals
            mu : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 : 0.001 :  None : False : False : PositiveReals
            rho : Size=1, Index=None
                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                None :     0 :   997 :  None : False : False : PositiveReals

        1 Block Declarations
            _gdp_relax_bigm : Size=1, Index=None, Active=True
                2 Block Declarations
                    re_transition : Size=1, Index=None, Active=True
                        1 Var Declarations
                            indicator_var : Size=1, Index=None
                                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                                None :     0 :  None :     1 : False :  True : Binary

                        5 Constraint Declarations
                            mixing_eq : Size=1, Index=None, Active=False
                                Key  : Lower : Body                                                                                                                                                 : Upper : Active
                                None :   0.0 : pre_mix.m_time - 33489.0 * pre_mix.dt**1.5 * pre_mix.H**0.5 * pre_mix.mu / ( pre_mix.rho * pre_mix.Po**0.666667 * pre_mix.N**2.0 * pre_mix.di**4.0 ) :   0.0 :  False
                            mixing_eq_hi : Size=1, Index=None, Active=True
                                Key  : Lower : Body                                                                                                                                                                                                                      : Upper : Active
                                None :  -Inf : pre_mix.m_time - 33489.0 * pre_mix.dt**1.5 * pre_mix.H**0.5 * pre_mix.mu / ( pre_mix.rho * pre_mix.Po**0.666667 * pre_mix.N**2.0 * pre_mix.di**4.0 ) - 1000.0*( 1 - pre_mix._gdp_relax_bigm.re_transition.indicator_var ) :   0.0 :   True
                            mixing_eq_lo : Size=1, Index=None, Active=True
                                Key  : Lower : Body                                                                                                                                                                                                                      : Upper : Active
                                None :   0.0 : pre_mix.m_time - 33489.0 * pre_mix.dt**1.5 * pre_mix.H**0.5 * pre_mix.mu / ( pre_mix.rho * pre_mix.Po**0.666667 * pre_mix.N**2.0 * pre_mix.di**4.0 ) + 1000.0*( 1 - pre_mix._gdp_relax_bigm.re_transition.indicator_var ) :  +Inf :   True
                            re_cons : Size=1, Index=None, Active=False
                                Key  : Lower : Body     : Upper  : Active
                                None :  -Inf : Reynolds : 9000.0 :  False
                            re_cons_eq : Size=1, Index=None, Active=True
                                Key  : Lower : Body                                                                          : Upper  : Active
                                None :  -Inf : Reynolds + 8000.0*( 1 - pre_mix._gdp_relax_bigm.re_transition.indicator_var ) : 9000.0 :   True

                        6 Declarations: indicator_var mixing_eq re_cons mixing_eq_lo mixing_eq_hi re_cons_eq
                    re_turbulent : Size=1, Index=None, Active=True
                        1 Var Declarations
                            indicator_var : Size=1, Index=None
                                Key  : Lower : Value : Upper : Fixed : Stale : Domain
                                None :     0 :  None :     1 : False :  True : Binary

                        5 Constraint Declarations
                            mixing_eq : Size=1, Index=None, Active=False
                                Key  : Lower : Body                                                                                                              : Upper : Active
                                None :   0.0 : pre_mix.m_time - 5.2 * pre_mix.dt**1.5 * pre_mix.H**0.5 / ( pre_mix.di**2.0 * pre_mix.Po**0.3333334 * pre_mix.N ) :   0.0 :  False
                            mixing_eq_hi : Size=1, Index=None, Active=True
                                Key  : Lower : Body                                                                                                                                                                                  : Upper : Active
                                None :  -Inf : pre_mix.m_time - 5.2 * pre_mix.dt**1.5 * pre_mix.H**0.5 / ( pre_mix.di**2.0 * pre_mix.Po**0.3333334 * pre_mix.N ) - 1000.0*( 1 - pre_mix._gdp_relax_bigm.re_turbulent.indicator_var ) :   0.0 :   True
                            mixing_eq_lo : Size=1, Index=None, Active=True
                                Key  : Lower : Body                                                                                                                                                                                  : Upper : Active
                                None :   0.0 : pre_mix.m_time - 5.2 * pre_mix.dt**1.5 * pre_mix.H**0.5 / ( pre_mix.di**2.0 * pre_mix.Po**0.3333334 * pre_mix.N ) + 1000.0*( 1 - pre_mix._gdp_relax_bigm.re_turbulent.indicator_var ) :  +Inf :   True
                            re_cons : Size=1, Index=None, Active=False
                                Key  : Lower   : Body     : Upper : Active
                                None : 10000.0 : Reynolds :  +Inf :  False
                            re_cons_eq : Size=1, Index=None, Active=True
                                Key  : Lower   : Body                                                                          : Upper : Active
                                None : 10000.0 : Reynolds + 10000.0*( 1 - pre_mix._gdp_relax_bigm.re_turbulent.indicator_var ) :  +Inf :   True

                        6 Declarations: indicator_var mixing_eq re_cons mixing_eq_lo mixing_eq_hi re_cons_eq

                2 Declarations: re_turbulent re_transition

        9 Declarations: di dt H rho mu Po N m_time _gdp_relax_bigm

1 Suffix Declarations
    BigM : Direction=Suffix.LOCAL, Datatype=Suffix.FLOAT
        Key  : Value
        None :  1000

4 Declarations: pre_mix Reynolds BigM _gdp_relax_bigm
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis/Rheology/processing$ cd ../../
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis$ git add .
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis$ git commit .
[master 491f088] 	modified:   Rheology/processing/premixing_models.py 	new file:   Rheology/processing/premixing_models.pyc 	modified:   Rheology/processing/premixing_models.py~ 	new file:   Rheology/processing/test_pre.py~ 	new file:   Rheology/processing/testing.py 	new file:   Rheology/processing/testing.py~ 	new file:   distest.py 	new file:   distest.py~
 8 files changed, 221 insertions(+), 140 deletions(-)
 rewrite Rheology/processing/premixing_models.py (86%)
 create mode 100644 Rheology/processing/premixing_models.pyc
 rewrite Rheology/processing/premixing_models.py~ (73%)
 create mode 100644 Rheology/processing/test_pre.py~
 create mode 100644 Rheology/processing/testing.py
 create mode 100644 Rheology/processing/testing.py~
 create mode 100644 distest.py
 create mode 100644 distest.py~
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis$ git push
Counting objects: 12, done.
Compressing objects: 100% (12/12), done.
Writing objects: 100% (12/12), 3.34 KiB | 0 bytes/s, done.
Total 12 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 2 local objects.        
To https://github.com/juantorres91/jj_thesis.git
   56b7d62..491f088  master -> master
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis$ python test.py
  File "test.py", line 42
    hzn = Chemical(name "hzl")
                            ^
SyntaxError: invalid syntax
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis$ python test.py
Traceback (most recent call last):
  File "test.py", line 120, in <module>
    m.k[i].value = m.DPh.Dmu.value / m.CPh.Dmu.value
TypeError: unsupported operand type(s) for /: 'NoneType' and 'float'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis$ python test.py
Ipopt 3.12.4: 

******************************************************************************
This program contains Ipopt, a library for large-scale nonlinear optimization.
 Ipopt is released as open source code under the Eclipse Public License (EPL).
         For more information visit http://projects.coin-or.org/Ipopt
******************************************************************************

This is Ipopt version 3.12.4, running with linear solver mumps.
NOTE: Other linear solvers might be more efficient (see Ipopt documentation).

Number of nonzeros in equality constraint Jacobian...:       96
Number of nonzeros in inequality constraint Jacobian.:        0
Number of nonzeros in Lagrangian Hessian.............:       38

Total number of variables............................:       42
                     variables with only lower bounds:       26
                variables with lower and upper bounds:       12
                     variables with only upper bounds:        0
Total number of equality constraints.................:       40
Total number of inequality constraints...............:        0
        inequality constraints with only lower bounds:        0
   inequality constraints with lower and upper bounds:        0
        inequality constraints with only upper bounds:        0

iter    objective    inf_pr   inf_du lg(mu)  ||d||  lg(rg) alpha_du alpha_pr  ls
   0 -9.9999900e-03 8.69e+04 2.00e+00  -1.0 0.00e+00    -  0.00e+00 0.00e+00   0
   1 -8.9550342e-03 3.08e+04 3.61e+04  -1.0 8.69e+04    -  3.63e-01 6.45e-01h  1
   2 -9.9666017e-03 2.10e+02 1.10e+04  -1.0 3.08e+04    -  4.84e-01 9.93e-01h  1
   3 -1.0194266e-02 4.67e-01 7.90e+01  -1.0 2.10e+02    -  9.89e-01 1.00e+00h  1
   4 -1.0166299e-02 7.94e-05 1.04e+03  -1.0 4.27e+01    -  6.48e-01 1.00e+00f  1
   5 -1.0431160e-02 2.22e-03 4.11e+02  -1.0 1.21e+02    -  6.04e-01 1.00e+00f  1
   6 -1.1168439e-02 1.65e-02 3.52e+02  -1.0 3.04e+02    -  4.92e-01 1.00e+00f  1
   7 -1.2656738e-02 5.99e-02 1.86e+02  -1.0 5.96e+02    -  6.77e-01 1.00e+00f  1
   8 -1.7123369e-02 4.55e-01 1.24e+02  -1.0 1.83e+03    -  5.41e-01 1.00e+00f  1
   9 -2.1126713e-02 2.02e-01 7.65e+00  -1.0 3.93e+03    -  9.21e-01 1.00e+00f  1
iter    objective    inf_pr   inf_du lg(mu)  ||d||  lg(rg) alpha_du alpha_pr  ls
  10 -1.8882970e-02 7.76e-02 3.28e+01  -1.0 4.20e+04    -  3.60e-01 1.00e+00f  1
  11 -1.9840810e-02 1.17e-02 4.17e+01  -1.0 5.13e+04    -  6.16e-01 1.00e+00f  1
  12 -1.9693659e-02 1.59e-03 1.59e+01  -1.0 7.97e+04    -  9.95e-01 1.00e+00f  1
  13 -1.9705526e-02 4.85e-04 6.22e+00  -1.0 1.17e+05    -  9.27e-01 1.00e+00f  1
  14 -1.9730156e-02 8.71e-06 2.49e-02  -1.7 5.31e+01    -  1.00e+00 1.00e+00h  1
  15 -1.9874709e-02 3.00e-04 4.59e+00  -3.8 3.75e+00    -  9.95e-01 1.00e+00h  1
  16 -2.1643914e-02 4.46e-02 7.76e-04  -3.8 1.34e+02    -  1.00e+00 9.48e-01h  1
  17 -2.1533853e-02 2.92e-04 6.60e-06  -3.8 1.06e+02    -  1.00e+00 1.00e+00h  1
  18 -2.1665667e-02 2.27e-04 1.83e-04  -5.7 1.88e+00    -  1.00e+00 1.00e+00h  1
  19 -2.1673432e-02 7.47e-07 6.56e-08  -5.7 2.09e-02    -  1.00e+00 1.00e+00h  1
iter    objective    inf_pr   inf_du lg(mu)  ||d||  lg(rg) alpha_du alpha_pr  ls
  20 -2.1675265e-02 4.38e-08 3.12e-08  -8.6 2.61e-02    -  1.00e+00 1.00e+00h  1
  21 -2.1675266e-02 2.13e-14 2.74e-14  -8.6 6.06e-04    -  1.00e+00 1.00e+00h  1

Number of Iterations....: 21

                                   (scaled)                 (unscaled)
Objective...............:  -2.1675266128943729e-02   -2.1675266128943729e-02
Dual infeasibility......:   2.7356483178217163e-14    2.7356483178217163e-14
Constraint violation....:   1.4210854715202004e-14    2.1316282072803006e-14
Complementarity.........:   2.5059035824745191e-09    2.5059035824745191e-09
Overall NLP error.......:   2.5059035824745191e-09    2.5059035824745191e-09


Number of objective function evaluations             = 22
Number of objective gradient evaluations             = 22
Number of equality constraint evaluations            = 22
Number of inequality constraint evaluations          = 0
Number of equality constraint Jacobian evaluations   = 22
Number of inequality constraint Jacobian evaluations = 0
Number of Lagrangian Hessian evaluations             = 21
Total CPU secs in IPOPT (w/o function evaluations)   =      0.004
Total CPU secs in NLP function evaluations           =      0.004

EXIT: Optimal Solution Found.
oldy : Size=2, Index=cd, Active=True
oldy[appl] : Active=True
    1 Set Declarations
        bounds_index : Dim=0, Dimen=1, Size=5, Domain=None, Ordered=False, Bounds=None
            [1, 2, 3, 4, 5]

    12 Var Declarations
        Nca : Size=1, Index=None
            Key  : Lower : Value     : Upper : Fixed : Stale : Domain
            None :     0 : 2.325e-05 :  None : False : False : PositiveReals
        Sr : Size=1, Index=None
            Key  : Lower : Value : Upper      : Fixed : Stale : Domain
            None :  10.0 : 100.0 : 10000000.0 : False : False :  Reals
        c_mu : Size=1, Index=None
            Key  : Lower : Value : Upper : Fixed : Stale : Domain
            None :     0 :  0.01 :  None : False : False : PositiveReals
        dD : Size=1, Index=None
            Key  : Lower : Value : Upper : Fixed : Stale : Domain
            None :   0.5 :   9.3 :   100 : False : False :  Reals
        k : Size=1, Index=None
            Key  : Lower : Value : Upper : Fixed : Stale : Domain
            None : 1e-07 : 100.0 :   300 : False : False :  Reals
        l1 : Size=1, Index=None
            Key  : Lower : Value         : Upper : Fixed : Stale : Domain
            None :  None : 96.9019413408 :  None : False : False :  Reals
        l2 : Size=1, Index=None
            Key  : Lower : Value         : Upper : Fixed : Stale : Domain
            None :  None : 95.3327315531 :  None : False : False :  Reals
        mu : Size=1, Index=None
            Key  : Lower : Value           : Upper : Fixed : Stale : Domain
            None :     0 : 0.0216752661289 :  None : False : False : PositiveReals
        st : Size=1, Index=None
            Key  : Lower : Value : Upper : Fixed : Stale : Domain
            None :     3 :  20.0 :   100 : False : False :  Reals
        v : Size=1, Index=None
            Key  : Lower : Value          : Upper : Fixed : Stale : Domain
            None : 0.001 : 0.348837153006 :   0.7 : False : False :  Reals
        y1 : Size=1, Index=None
            Key  : Lower : Value         : Upper : Fixed : Stale : Domain
            None :     0 : 2.16752679106 :  None : False : False : PositiveReals
        y2 : Size=1, Index=None
            Key  : Lower : Value          : Upper : Fixed : Stale : Domain
            None :     0 : 0.999999917803 :  None : False : False : PositiveReals

    6 Constraint Declarations
        Nca_def : Size=1, Index=None, Active=True
            Key  : Lower : Body                                                                                             : Upper : Active
            None :   0.0 : 0.002 * oldy[appl].Nca * oldy[appl].st - 1e-07 * oldy[appl].c_mu * oldy[appl].dD * oldy[appl].Sr :   0.0 :   True
        l1_def : Size=1, Index=None, Active=True
            Key  : Lower : Body                                                                                                                                                                                                     : Upper : Active
            None :   0.0 : oldy[appl].l1 - ( 16 + 19*oldy[appl].k ) * ( 3 + 2*oldy[appl].k ) * ( 1 + 0.2 * ( 16 + 19*oldy[appl].k ) * oldy[appl].v / ( ( 1 + oldy[appl].k ) * ( 3 + 2*oldy[appl].k ) ) ) / ( 40 + 40*oldy[appl].k ) :   0.0 :   True
        l2_def : Size=1, Index=None, Active=True
            Key  : Lower : Body                                                                                                                                                                                                     : Upper : Active
            None :   0.0 : oldy[appl].l2 - ( 16 + 19*oldy[appl].k ) * ( 3 + 2*oldy[appl].k ) * ( 1 - 0.3 * ( 16 + 19*oldy[appl].k ) * oldy[appl].v / ( ( 1 + oldy[appl].k ) * ( 3 + 2*oldy[appl].k ) ) ) / ( 40 + 40*oldy[appl].k ) :   0.0 :   True
        mu_def : Size=1, Index=None, Active=True
            Key  : Lower : Body                                                            : Upper : Active
            None :   0.0 : oldy[appl].mu - oldy[appl].c_mu * oldy[appl].y1 * oldy[appl].y2 :   0.0 :   True
        y1_def : Size=1, Index=None, Active=True
            Key  : Lower : Body                                                                                                                                                                        : Upper : Active
            None :   0.0 : -1 + oldy[appl].y1 - 0.5 * ( 2 + 5*oldy[appl].k ) * oldy[appl].v / ( 1 + oldy[appl].k ) - 0.1 * ( 2 + 5*oldy[appl].k )**2.0 * oldy[appl].v**2.0 / ( 1 + oldy[appl].k )**2.0 :   0.0 :   True
        y2_def : Size=1, Index=None, Active=True
            Key  : Lower : Body                                                                                                                           : Upper : Active
            None :   0.0 : oldy[appl].y2 - ( 1 + oldy[appl].l1 * oldy[appl].l2 * oldy[appl].Nca**2.0 ) / ( 1 + oldy[appl].l1**2.0 * oldy[appl].Nca**2.0 ) :   0.0 :   True

    19 Declarations: l1 l2 Nca y1 y2 Sr st dD v k c_mu mu l1_def l2_def y1_def y2_def Nca_def mu_def bounds_index
oldy[prop] : Active=True
    1 Set Declarations
        bounds_index : Dim=0, Dimen=1, Size=5, Domain=None, Ordered=False, Bounds=None
            [1, 2, 3, 4, 5]

    12 Var Declarations
        Nca : Size=1, Index=None
            Key  : Lower : Value           : Upper : Fixed : Stale : Domain
            None :     0 : 0.0689906251171 :  None : False : False : PositiveReals
        Sr : Size=1, Index=None
            Key  : Lower : Value         : Upper      : Fixed : Stale : Domain
            None :  10.0 : 296733.871471 : 10000000.0 : False : False :  Reals
        c_mu : Size=1, Index=None
            Key  : Lower : Value : Upper : Fixed : Stale : Domain
            None :     0 :  0.01 :  None : False : False : PositiveReals
        dD : Size=1, Index=None
            Key  : Lower : Value : Upper : Fixed : Stale : Domain
            None :   0.5 :   9.3 :   100 : False : False :  Reals
        k : Size=1, Index=None
            Key  : Lower : Value : Upper : Fixed : Stale : Domain
            None : 1e-07 : 100.0 :   300 : False : False :  Reals
        l1 : Size=1, Index=None
            Key  : Lower : Value         : Upper : Fixed : Stale : Domain
            None :  None : 96.9019413408 :  None : False : False :  Reals
        l2 : Size=1, Index=None
            Key  : Lower : Value         : Upper : Fixed : Stale : Domain
            None :  None : 95.3327315531 :  None : False : False :  Reals
        mu : Size=1, Index=None
            Key  : Lower : Value           : Upper : Fixed : Stale : Domain
            None :     0 : 0.0213319448606 :  None : False : False : PositiveReals
        st : Size=1, Index=None
            Key  : Lower : Value : Upper : Fixed : Stale : Domain
            None :     3 :  20.0 :   100 : False : False :  Reals
        v : Size=1, Index=None
            Key  : Lower : Value          : Upper : Fixed : Stale : Domain
            None : 0.001 : 0.348837153006 :   0.7 : False : False :  Reals
        y1 : Size=1, Index=None
            Key  : Lower : Value         : Upper : Fixed : Stale : Domain
            None :     0 : 2.16752679106 :  None : False : False : PositiveReals
        y2 : Size=1, Index=None
            Key  : Lower : Value          : Upper : Fixed : Stale : Domain
            None :     0 : 0.984160608699 :  None : False : False : PositiveReals

    6 Constraint Declarations
        Nca_def : Size=1, Index=None, Active=True
            Key  : Lower : Body                                                                                             : Upper : Active
            None :   0.0 : 0.002 * oldy[prop].Nca * oldy[prop].st - 1e-07 * oldy[prop].c_mu * oldy[prop].dD * oldy[prop].Sr :   0.0 :   True
        l1_def : Size=1, Index=None, Active=True
            Key  : Lower : Body                                                                                                                                                                                                     : Upper : Active
            None :   0.0 : oldy[prop].l1 - ( 16 + 19*oldy[prop].k ) * ( 3 + 2*oldy[prop].k ) * ( 1 + 0.2 * ( 16 + 19*oldy[prop].k ) * oldy[prop].v / ( ( 1 + oldy[prop].k ) * ( 3 + 2*oldy[prop].k ) ) ) / ( 40 + 40*oldy[prop].k ) :   0.0 :   True
        l2_def : Size=1, Index=None, Active=True
            Key  : Lower : Body                                                                                                                                                                                                     : Upper : Active
            None :   0.0 : oldy[prop].l2 - ( 16 + 19*oldy[prop].k ) * ( 3 + 2*oldy[prop].k ) * ( 1 - 0.3 * ( 16 + 19*oldy[prop].k ) * oldy[prop].v / ( ( 1 + oldy[prop].k ) * ( 3 + 2*oldy[prop].k ) ) ) / ( 40 + 40*oldy[prop].k ) :   0.0 :   True
        mu_def : Size=1, Index=None, Active=True
            Key  : Lower : Body                                                            : Upper : Active
            None :   0.0 : oldy[prop].mu - oldy[prop].c_mu * oldy[prop].y1 * oldy[prop].y2 :   0.0 :   True
        y1_def : Size=1, Index=None, Active=True
            Key  : Lower : Body                                                                                                                                                                        : Upper : Active
            None :   0.0 : -1 + oldy[prop].y1 - 0.5 * ( 2 + 5*oldy[prop].k ) * oldy[prop].v / ( 1 + oldy[prop].k ) - 0.1 * ( 2 + 5*oldy[prop].k )**2.0 * oldy[prop].v**2.0 / ( 1 + oldy[prop].k )**2.0 :   0.0 :   True
        y2_def : Size=1, Index=None, Active=True
            Key  : Lower : Body                                                                                                                           : Upper : Active
            None :   0.0 : oldy[prop].y2 - ( 1 + oldy[prop].l1 * oldy[prop].l2 * oldy[prop].Nca**2.0 ) / ( 1 + oldy[prop].l1**2.0 * oldy[prop].Nca**2.0 ) :   0.0 :   True

    19 Declarations: l1 l2 Nca y1 y2 Sr st dD v k c_mu mu l1_def l2_def y1_def y2_def Nca_def mu_def bounds_index
mass_flow : Size=1, Index=None
    Key  : Lower : Value         : Upper : Fixed : Stale : Domain
    None :     0 : 70.0000052046 :  None : False : False : PositiveReals
k : Size=2, Index=cd
    Key  : Lower : Value : Upper : Fixed : Stale : Domain
    appl :     0 : 100.0 :  None : False : False : PositiveReals
    prop :     0 : 100.0 :  None : False : False : PositiveReals
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis$ python test.py
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis$ python test.py
Traceback (most recent call last):
  File "test.py", line 120, in <module>
    m.k[i].value = m.DPh.Dmu.value / m.CPh.Dmu.value
TypeError: unsupported operand type(s) for /: 'NoneType' and 'float'
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis$ python test.py
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis$ python test.py
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis$ python test.py
mass_balance : Size=1, Index=None, Active=True
    Key  : Lower : Body              : Upper : Active
    None :   1.0 : xw[hzl] + xw[oil] :   1.0 :   True
(pysp_test) juan@juan-VirtualBox:~/Desktop/jj_thesis$ git 