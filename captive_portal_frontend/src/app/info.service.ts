import { Injectable } from '@angular/core';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import { ConnectionService } from './connection.service';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';

@Injectable()
export class InfoService {
  constructor(private router: Router, private http:Http, private connectionLink: ConnectionService, private cookie: CookieService) {
    
  }

  addInfo(newInfo: any, $: any){
    return this.http.post(this.connectionLink.getConnection()+'/info ', newInfo)
    .toPromise()
    .then(res =>res.json())
    .then(resJson => {
      console.log(resJson);
      if (resJson.error_code == 0){
        this.router.navigate(['check']);
      }
      else{
        $("#errorLabel").text(resJson.message);
      } 
    });
  }

  checkDigit(digit: any, $: any){
    console.log(digit);
    return this.http.post(this.connectionLink.getConnection()+'/check ', digit)
    .toPromise()
    .then(res =>res.json())
    .then(resJson => {
      alert(resJson.message);
    });
  }

}