import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from '../components/home/Home';
import Challan from '../components/challan/Challan';
import Police from '../components/police/Police';
import Query from '../components/query/Query';
import CheckList from '../components/checkList/CheckList';
import Check from '../components/check/Check';
import QueryList from '../components/queryList/QueryList';
import QueryDisplay from '../components/queryDisplay/QueryDisplay';

const AppRouter = () => (
  <>
  <nav class="navbar navbar-dark bg-dark sticky-top">
  <a class="navbar-brand" href="#" style={{fontSize: "40px"}}>Road Duty</a>
  </nav>
  <BrowserRouter>
    <div className="container">
      <Switch>
        <Route component={Home} path="/" exact />
        <Route component={Police} path="/police" exact />

        <Route component={Challan} path="/challan/:challanId" />

        <Route component={Query} path="/raise_query/:challanId" />

        <Route component={QueryList} path="/query/" exact />
        <Route component={QueryDisplay} path="/query/:id" />
        
        <Route component={CheckList} path="/check" exact />
        <Route component={Check} path="/check/:challanId" />
      </Switch>
    </div>
  </BrowserRouter>
  </>
);

export default AppRouter;
