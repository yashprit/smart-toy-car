import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Socket } from 'ng-socket-io';
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  canvas:any;

  constructor(public navCtrl: NavController, private socket: Socket) {
    this.canvas = null;
    this.getMessages().subscribe(message => {
      console.log(message);
      /*const context = this.canvas.getContext('2d');
      const img = new Image();
      const canvas = this.canvas;
      img.onload = function() {
        context.drawImage(this, 0, 0, canvas.width, canvas.height);
      }
      img.src = `data:image/png;base64,${message}`*/
    });
  }

  showVideo() {
    this.canvas = document.getElementById("video");
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
