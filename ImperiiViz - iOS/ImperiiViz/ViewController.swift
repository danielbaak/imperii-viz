//
//  ViewController.swift
//  ImperiiViz
//
//  Created by Frederik Riedel on 26.04.15.
//  Copyright (c) 2015 Frederik Riedel. All rights reserved.
//

import UIKit
import MapKit

class ViewController: UIViewController,UITextFieldDelegate,TimeLineViewDelegate {

    var dateIndicator : DateIndicator?
    var mapView: MKMapView?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.view.backgroundColor=UIColor.whiteColor()
        
        //var backgroundImage = UIImageView(frame: CGRectMake(0, 0, self.view.frame.width, self.view.frame.height))
        //backgroundImage.image=UIImage(named: "Startpage")
        //self.view.addSubview(backgroundImage)
        
        /*var suchfled = UITextField(frame: CGRectMake((self.view.frame.width-400)/2, (self.view.frame.height-44)/2, 400, 44))
        suchfled.backgroundColor=UIColor.darkGrayColor()
        self.view.addSubview(suchfled)*/
        
        NSNotificationCenter.defaultCenter().addObserver(self, selector:"keyboardWillChange:", name:UIKeyboardWillChangeFrameNotification, object:nil)
        
        
        var from = NSDateComponents()
        from.year = 600
        
        var to = NSDateComponents()
        to.year = 1600
        
        mapView = MKMapView(frame: self.view.frame)
        mapView!.mapType = MKMapType.Satellite
        mapView!.showsPointsOfInterest = false
        mapView!.zoomEnabled = true
        mapView!.scrollEnabled = true
        self.view.addSubview(mapView!)
        
        
        var timeLineView = TimeLineView(frame: CGRectMake(0, self.view.frame.height-75, self.view.frame.size.width, 75), from: from, to: to)
        timeLineView.delegate=self
        self.view.addSubview(timeLineView)
        
        dateIndicator = DateIndicator(frame: CGRectMake(100, timeLineView.frame.origin.y-55 + 15, 100, 55))
        self.view.addSubview(dateIndicator!)
        
        
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    func yearChanged(year: Float, position: CGPoint) {
        dateIndicator?.frame=CGRectMake(position.x, dateIndicator!.frame.origin.y, dateIndicator!.frame.width, dateIndicator!.frame.height)
        dateIndicator?.center=CGPointMake(position.x, dateIndicator!.center.y)
        dateIndicator?.setYear(year)
    }
    
    
}

