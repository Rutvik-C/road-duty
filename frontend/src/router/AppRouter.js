import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from '../components/home/Home';
import Challan from '../components/challan/Challan';
import Query from '../components/query/Query';
import CheckList from '../components/checkList/CheckList';
import Check from '../components/check/Check';
import QueryList from '../components/queryList/QueryList';

const AppRouter = () => (
  <BrowserRouter>
    <div className="container">
      <Switch>
        <Route component={Home} path="/" exact />
        <Route component={Challan} path="/challan/:challanId" />

        <Route component={QueryList} path="/query/" exact />
        <Route component={Query} path="/query/:challanId" />
        
        <Route component={CheckList} path="/check" exact />
        <Route component={Check} path="/check/:challanId" />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;
