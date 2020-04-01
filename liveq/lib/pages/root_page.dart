import 'package:flutter/material.dart';
import 'package:liveq/widgets/lq_next_button.dart';
import 'package:liveq/utils/routing_constants.dart';

class RootPage extends StatelessWidget {
  RootPage({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'LiveQ',
              style: Theme.of(context).textTheme.headline4.merge(
                    TextStyle(fontWeight: FontWeight.bold),
                  ),
            ),
            SizedBox(height: 150),
            // NextButton('JOIN A ROOM'),
            NextButton(
                'JOIN A ROOM', Navigator.pushNamed(context, JoinRoomPageRoute)),
            // NextButton('CREATE NEW ROOM'),
            // NextButton('CREATE NEW ROOM',
            //     Navigator.pushNamed(context, ServicesPageRoute)),
          ],
        ),
      ),
    );
  }
}
