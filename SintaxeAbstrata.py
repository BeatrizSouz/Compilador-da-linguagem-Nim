
type
  Visitor* = ref object of RootObj

type
  # Bases
  Program*          = ref object of RootObj
  GlobalVarDecl*    = ref object of RootObj
  CallGlobal*       = ref object of RootObj
  FuncDecl*         = ref object of RootObj
  Signature*        = ref object of RootObj
  SigParams*        = ref object of RootObj
  Body*             = ref object of RootObj
  Stms*             = ref object of RootObj
  Stm*              = ref object of RootObj
  Exp*              = ref object of RootObj
  Call*             = ref object of RootObj
  Params*           = ref object of RootObj

  # Program
  CompoundFunProgram* = ref object of Program
    funcDecl*: FuncDecl
    program*: Program
  CompoundVarProgram* = ref object of Program
    globalVarDecl*: GlobalVarDecl
    program*: Program
  CompoundCallProgram* = ref object of Program
    callglobal*: CallGlobal
    program*: Program
  SingleFunProgram* = ref object of Program
    funcDecl*: FuncDecl
  SingleVarProgram* = ref object of Program
    globalVarDecl*: GlobalVarDecl
  SingleCallProgram* = ref object of Program
    callglobal*: CallGlobal

  # GlobalVarDecl
  GVDConcrete* = ref object of GlobalVarDecl
    id*: string
    exp*: Exp

  # CallGlobal
  CGCConcrete* = ref object of CallGlobal
    call*: Call

  # FuncDecl
  FuncDeclConcrete* = ref object of FuncDecl
    signature*: Signature
    body*: Body

  # Signature
  SignatureConcrete* = ref object of Signature
    typ*: string       # "type" é palavra-chave em Nim; usei "typ"
    id*: string
    sigParams*: SigParams

  # SigParams
  SingleSigParams* = ref object of SigParams
    typ*: string
    id*: string
  CompoundSigParams* = ref object of SigParams
    typ*: string
    id*: string
    sigParams*: SigParams

  # Body
  BodyConcrete* = ref object of Body
    stms*: Stms

  # Stms
  SingleStm* = ref object of Stms
    stm*: Stm
  CompoundStm* = ref object of Stms
    stm*: Stm
    stms*: Stms

  # Stm
  StmExp* = ref object of Stm
    exp*: Exp
  StmWhile* = ref object of Stm
    exp*: Exp
    block*: Stms
  StmReturn* = ref object of Stm
    exp*: Exp

  # Exp
  AssignExp* = ref object of Exp
    exp1*: Exp
    exp2*: Exp
  LessExp* = ref object of Exp
    exp1*: Exp
    exp2*: Exp
  SomaExp* = ref object of Exp
    exp1*: Exp
    exp2*: Exp
  MulExp* = ref object of Exp
    exp1*: Exp
    exp2*: Exp
  PotExp* = ref object of Exp
    exp1*: Exp
    exp2*: Exp

  CallExp* = ref object of Exp
    call*: Call

  NumExp* = ref object of Exp
    num*: int
  IdExp* = ref object of Exp
    id*: string
  BooleanExp* = ref object of Exp
    boolValue*: bool

  # Call
  ParamsCall* = ref object of Call
    id*: string
    params*: Params
  NoParamsCall* = ref object of Call
    id*: string

  # Params
  CompoundParams* = ref object of Params
    exp*: Exp
    params*: Params
  SingleParam* = ref object of Params
    exp*: Exp


# -------------------------------
# Métodos "visitX" do Visitor (abstratos/base)
# -------------------------------

# Program
method visitCompoundFunProgram*(v: Visitor, n: CompoundFunProgram) {.base.} = discard
method visitCompoundVarProgram*(v: Visitor, n: CompoundVarProgram) {.base.} = discard
method visitCompoundCallProgram*(v: Visitor, n: CompoundCallProgram) {.base.} = discard
method visitSingleFunProgram*(v: Visitor, n: SingleFunProgram) {.base.} = discard
method visitSingleVarProgram*(v: Visitor, n: SingleVarProgram) {.base.} = discard
method visitSingleCallProgram*(v: Visitor, n: SingleCallProgram) {.base.} = discard

# GlobalVarDecl
method visitGVDConcrete*(v: Visitor, n: GVDConcrete) {.base.} = discard

# CallGlobal
method visitCGCConcrete*(v: Visitor, n: CGCConcrete) {.base.} = discard

# FuncDecl
method visitFuncDeclConcrete*(v: Visitor, n: FuncDeclConcrete) {.base.} = discard

# Signature
method visitSignatureConcrete*(v: Visitor, n: SignatureConcrete) {.base.} = discard

# SigParams
method visitSingleSigParams*(v: Visitor, n: SingleSigParams) {.base.} = discard
method visitCompoundSigParams*(v: Visitor, n: CompoundSigParams) {.base.} = discard

# Body
method visitBodyConcrete*(v: Visitor, n: BodyConcrete) {.base.} = discard

# Stms
method visitSingleStm*(v: Visitor, n: SingleStm) {.base.} = discard
method visitCompoundStm*(v: Visitor, n: CompoundStm) {.base.} = discard

# Stm
method visitStmExp*(v: Visitor, n: StmExp) {.base.} = discard
method visitStmWhile*(v: Visitor, n: StmWhile) {.base.} = discard
method visitStmReturn*(v: Visitor, n: StmReturn) {.base.} = discard

# Exp
method visitAssignExp*(v: Visitor, n: AssignExp) {.base.} = discard
method visitLessExp*(v: Visitor, n: LessExp) {.base.} = discard
method visitSomaExp*(v: Visitor, n: SomaExp) {.base.} = discard
method visitMulExp*(v: Visitor, n: MulExp) {.base.} = discard
method visitPotExp*(v: Visitor, n: PotExp) {.base.} = discard
method visitCallExp*(v: Visitor, n: CallExp) {.base.} = discard
method visitNumExp*(v: Visitor, n: NumExp) {.base.} = discard
method visitIdExp*(v: Visitor, n: IdExp) {.base.} = discard
method visitBooleanExp*(v: Visitor, n: BooleanExp) {.base.} = discard

# Call
method visitParamsCall*(v: Visitor, n: ParamsCall) {.base.} = discard
method visitNoParamsCall*(v: Visitor, n: NoParamsCall) {.base.} = discard

# Params
method visitCompoundParams*(v: Visitor, n: CompoundParams) {.base.} = discard
method visitSingleParam*(v: Visitor, n: SingleParam) {.base.} = discard


# -------------------------------
# Métodos accept (base abstratos)
# -------------------------------
method accept*(self: Program; v: Visitor) {.base.} = discard
method accept*(self: GlobalVarDecl; v: Visitor) {.base.} = discard
method accept*(self: CallGlobal; v: Visitor) {.base.} = discard
method accept*(self: FuncDecl; v: Visitor) {.base.} = discard
method accept*(self: Signature; v: Visitor) {.base.} = discard
method accept*(self: SigParams; v: Visitor) {.base.} = discard
method accept*(self: Body; v: Visitor) {.base.} = discard
method accept*(self: Stms; v: Visitor) {.base.} = discard
method accept*(self: Stm; v: Visitor) {.base.} = discard
method accept*(self: Exp; v: Visitor) {.base.} = discard
method accept*(self: Call; v: Visitor) {.base.} = discard
method accept*(self: Params; v: Visitor) {.base.} = discard


# Program
method accept*(self: CompoundFunProgram; v: Visitor) = v.visitCompoundFunProgram(self)
method accept*(self: CompoundVarProgram; v: Visitor) = v.visitCompoundVarProgram(self)
method accept*(self: CompoundCallProgram; v: Visitor) = v.visitCompoundCallProgram(self)
method accept*(self: SingleFunProgram; v: Visitor) = v.visitSingleFunProgram(self)
method accept*(self: SingleVarProgram; v: Visitor) = v.visitSingleVarProgram(self)
method accept*(self: SingleCallProgram; v: Visitor) = v.visitSingleCallProgram(self)

# GlobalVarDecl
method accept*(self: GVDConcrete; v: Visitor) = v.visitGVDConcrete(self)

# CallGlobal
method accept*(self: CGCConcrete; v: Visitor) = v.visitCGCConcrete(self)

# FuncDecl
method accept*(self: FuncDeclConcrete; v: Visitor) = v.visitFuncDeclConcrete(self)

# Signature
method accept*(self: SignatureConcrete; v: Visitor) = v.visitSignatureConcrete(self)

# SigParams
method accept*(self: SingleSigParams; v: Visitor) = v.visitSingleSigParams(self)
method accept*(self: CompoundSigParams; v: Visitor) = v.visitCompoundSigParams(self)

# Body
method accept*(self: BodyConcrete; v: Visitor) = v.visitBodyConcrete(self)

# Stms
method accept*(self: SingleStm; v: Visitor) = v.visitSingleStm(self)
method accept*(self: CompoundStm; v: Visitor) = v.visitCompoundStm(self)

# Stm
method accept*(self: StmExp; v: Visitor) = v.visitStmExp(self)
method accept*(self: StmWhile; v: Visitor) = v.visitStmWhile(self)
method accept*(self: StmReturn; v: Visitor) = v.visitStmReturn(self)

# Exp
method accept*(self: AssignExp; v: Visitor) = v.visitAssignExp(self)
method accept*(self: LessExp; v: Visitor) = v.visitLessExp(self)
method accept*(self: SomaExp; v: Visitor) = v.visitSomaExp(self)
method accept*(self: MulExp; v: Visitor) = v.visitMulExp(self)
method accept*(self: PotExp; v: Visitor) = v.visitPotExp(self)
method accept*(self: CallExp; v: Visitor) = v.visitCallExp(self)
method accept*(self: NumExp; v: Visitor) = v.visitNumExp(self)
method accept*(self: IdExp; v: Visitor) = v.visitIdExp(self)
method accept*(self: BooleanExp; v: Visitor) = v.visitBooleanExp(self)

# Call
method accept*(self: ParamsCall; v: Visitor) = v.visitParamsCall(self)
method accept*(self: NoParamsCall; v: Visitor) = v.visitNoParamsCall(self)

# Params
method accept*(self: CompoundParams; v: Visitor) = v.visitCompoundParams(self)
method accept*(self: SingleParam; v: Visitor) = v.visitSingleParam(self)



# Adiciona código em Nim
