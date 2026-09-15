# Sample Flutter diff (fixture)

Stand-in for a pasted PR diff. Not from a real repo.

```diff
--- a/lib/main.dart
+++ b/lib/main.dart
@@ -40,7 +40,10 @@ class _MyHomePageState extends State<MyHomePage> {
-    onPressed: () {
-      setState(() {
-        _counter++;
-      });
-    },
+    onPressed: () async {
+      await Future<void>.delayed(Duration.zero);
+      setState(() {
+        _counter++;
+      });
+    },
```

Notes for review: after an async gap, `mounted` should be checked before `setState`. No live `fvm flutter test` was run in the fixture itself.
