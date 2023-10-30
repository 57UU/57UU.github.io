---
title: Flutter局部跳转
date: 2023-10-30 13:27:01
tags: Flutter Coding
---


`flutter`局部跳转的思路其实很简单,只需要在一个控件外创建一个根路由,仿照安卓的命名,我给这个路由起名叫`Fragment`
```dart
class Fragment extends StatelessWidget {
  final Widget child;
  final String root;

  const Fragment({required this.child, this.root = "/", super.key});

  @override
  Widget build(BuildContext context) {
    return Navigator(
      initialRoute: root,
      onGenerateRoute: (RouteSettings settings) {
        WidgetBuilder builder;
        builder = (context) => child;
        return MaterialPageRoute(builder: builder);
      },
    );
  }
}
```
这段代码来自[这里](https://github.com/57UU/Shape_Weather/blob/master/lib/WeatherUI/Control.dart)

效果如[Shape_Weather](https://57uu.github.io/Shape_Weather/)