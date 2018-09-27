import { Injectable } from '@angular/core';

@Injectable()
export class ConnectionService {

  constructor() { }

  getConnection():string{

    return 'http://10.19.1.44:8080';
  }

}
