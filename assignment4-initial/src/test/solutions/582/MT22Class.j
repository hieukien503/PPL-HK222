.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label2:
	iconst_1
	ifle Label3
	iload_1
	bipush 20
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	goto Label3
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
	iload_1
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 7
.limit locals 2
.end method
