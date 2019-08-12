import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Socket } from 'ng-socket-io';
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  constructor(public navCtrl: NavController, private socket: Socket) {
    this.getMessages().subscribe(message => {
      console.log(message);
    });
  }

  showVideo() {
    this.socket.connect();
    this.socket.emit('video');
  }

  getMessages() {
    let observable = new Observable(observer => {
      this.socket.on('frame', (data) => {
        observer.next(data);
      });
    })
    return observable;
  }

}
